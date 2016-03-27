
schema =  {
         'username': {
             'type': 'string',
             'required': True,
             'unique': True,
             },
         'password': {
             'type': 'string',
             'required': True,
         },
         'email': {
             'type': 'string',
             'required': True,
             },
         'role': {
             'type': 'string',
             'allowed': ['player', 'mod', 'admin'],
             'default': 'player',
         }
     }

accounts = {
    # the standard account entry point is defined as
    # '/accounts/<ObjectId>'. We define  an additional read-only entry
    # point accessible at '/accounts/<username>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
        'allowed_roles': ['mod', 'admin'],
    },

    # We also disable endpoint caching as we don't want client apps to
    # cache account data.
    'cache_control': '',
    'cache_expires': 0,

    # Only allow superusers and admins.
    'allowed_roles': ['mod', 'admin'],

    # Finally, let's add the schema definition for this endpoint.
    'schema': schema,
}


