# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports

# App imports
from mrerp.employees.factories import EmployeeFactory
from mrerp.employees.models import Employee
from mrerp.issues_management.epics.factories import EpicFactory
from mrerp.graphqls.tests.base import BaseTest
from mrerp.phases.factories import PhaseFactory


class ListEpicTest(BaseTest):
    def test_list_epics(self):
        epics = EpicFactory.create_batch(20, jiraissue=None)
        admin = EmployeeFactory(role=Employee.EMPLOYEE_ROLE_ADMIN)
        self.client.force_login(user=admin.user)
        query = ''' 
            query {
                getEpics{
                    edges{
                        node{
                            id
                            name
                        }
                    }
                    totalCount
                }
            }
        '''
        response = self.client.execute(query)
        self.assertFalse(response.errors)

        query_data = response.data['getEpics']['edges']
        count = response.data['getEpics']['totalCount']
        self.assertTrue(query_data)
        self.assertEqual(count, 20)

        for epic in epics:
            epic_id = self.to_global_id(epic)
            query_epic = next(
                (query_epic for query_epic in query_data if
                 query_epic['node']['id'] == epic_id), None)

            self.assertTrue(query_epic)
            epic_data = query_epic['node']
            self.assertEqual(epic_data['id'], epic_id)
            self.assertEqual(epic_data['name'], epic.name)

    def test_list_epics_by_phase(self):
        epics_other_phases = EpicFactory.create_batch(5, jiraissue=None)
        phase = PhaseFactory(name='TEST')
        phase_id = self.to_global_id(phase)
        epics = EpicFactory.create_batch(5, phase=phase, jiraissue=None)
        admin = EmployeeFactory(role=Employee.EMPLOYEE_ROLE_ADMIN)
        self.client.force_login(user=admin.user)
        query = ''' 
            query {
                getEpics(phase: "%s"){
                    edges{
                        node{
                            id
                            name
                            phase {
                                id
                                name
                            }
                        }
                    }
                    totalCount
                }
            }
        ''' % phase_id
        response = self.client.execute(query)
        self.assertFalse(response.errors)

        query_data = response.data['getEpics']['edges']
        count = response.data['getEpics']['totalCount']
        self.assertTrue(query_data)
        self.assertEqual(count, 5)

        for epic in epics:
            epic_id = self.to_global_id(epic)
            query_epic = next(
                (query_epic for query_epic in query_data if
                 query_epic['node']['id'] == epic_id), None)

            self.assertTrue(query_epic)
            epic_data = query_epic['node']
            self.assertEqual(epic_data['id'], epic_id)
            self.assertEqual(epic_data['name'], epic.name)
            self.assertEqual(epic_data['phase']['id'], phase_id)
            self.assertEqual(epic_data['phase']['name'], phase.name)
