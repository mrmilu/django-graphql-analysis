# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports

# App imports

QUERY_ALL_CARTS = '''
    {
      allCarts {
        edges {
          node {
            id
            name
            description
          }
        }
        totalCount
      }
    }
'''
