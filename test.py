import pygrakn as grakn

def test_basic_genealogy():
    '''Simple test based on the Grakn quickstart tutorial

    >>> test_basic_genealogy()
    Got person entity with 4 attributes.
    '''
    with grakn.Graph(keyspace='grakn') as graph:
        result = graph.execute('match $p isa person, has identifier "Mary Guthrie"; get;')
        # [{'id': 'V61480', 'base_type': 'entity', 'type': 'person', 'attributes':
        #  [{'id': 'V53368', 'label': 'gender', 'value': 'female'},
        #   {'id': 'V65576', 'label': 'firstname', 'value': 'Mary'},
        #   {'id': 'V73776', 'label': 'surname', 'value': 'Guthrie'},
        #   {'id': 'V98312', 'label': 'identifier', 'value': 'Mary Guthrie'}]
        # }]
        print('Got {} {} with {} attributes.'.format(result[0]['type'], result[0]['base_type'], len(result[0]['attributes'])))

