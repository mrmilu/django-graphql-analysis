# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports

# App imports
from shop_demo.django_graphql.tests import SchemaTestCaseGQLContext
from shop_demo.users.factories import UserFactory


class GetProductTest(SchemaTestCaseGQLContext):
    def test_get_product(self):
        user = UserFactory()
        self.client.force_login(user=user)
        query = '''
            query {
              product(id: "%s") {
                id
                name                
                phase {
                    id
                    name
                }
                resolution
                consumption
                deviation
                userStories{
                  edges{
                    node{
                      id
                      name
                    }
                  }
                }
              }
            }
        ''' % product_id
        response = self.client.execute(query)
        self.assertFalse(response.errors)

        query_data = response.data['product']
        self.assertTrue(response.data['product'])

        self.assertEqual(query_data['id'], product_id)
        self.assertEqual(query_data['name'], product.name)

        self.assertEqual(query_data['resolution'], product.resolution)
        self.assertEqual(query_data['consumption'], product.consumption)
        self.assertEqual(query_data['deviation'], product.deviation)

        self.assertEqual(query_data['phase']['id'], self.to_global_id(product.phase))
        self.assertEqual(query_data['phase']['name'], product.phase.name)
