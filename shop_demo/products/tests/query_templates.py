# -*- coding: utf-8 -*-
# Python imports

# 3rd Party imports

# App imports

QUERY_ALL_PRODUCTS = '''
{
  products {
    edges {
      node {
        id
        name
        description
        variants {
          edges{
            node {
              id
              display_name
              size
              color
              prize       
            }
          }
        }
      }
    }
    totalCount
  }
}
'''

QUERY_FILTERED_PRODUCTS = '''
{
  products (%s) {
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

QUERY_PRODUCT = '''
{
  product(id: "%s") {        
    id
    name
    description
    variants {
      edges{
        node {
          id
          display_name
          size
          color
          prize       
        }
      }
    }
  }
}
'''

QUERY_PRODUCT_LITE = '''
{
  product(id: "%s") {        
    id
    name
    description    
  }
}
'''

QUERY_MULTIPLE_PRODUCTS_WITH_ALIAS = '''
{
  %s: product(id: "%s") {
    name
    description
  }
  %s: product(id: "%s") {
    name
    description
  }
}
'''

UPDATE_PRODUCT = '''
mutation productUpdate($input: ProductInput!) {
  productUpdate(input: $input) {
    product {
      id
    }
    errors {
      field
      message
    }
  }
}
'''
