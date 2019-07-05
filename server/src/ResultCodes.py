
class ResultCodes():

    # result codes for SignupHandler
    ERROR_USERNAME_LENGTH_INVALID          = 'INVALID_USERNAME_LENGTH'
    ERROR_PASSWORD_LENGTH_INVALID          = 'INVALID_PASSWORD_LENGTH'
    ERROR_INVALID_USERNAME_CHARS           = 'INVALID_USERNAME_CHARS'
    ERROR_DUPLICATE_USERNAME               = 'DUPLICATE_USERNAME'
    ERROR_EMPTY_USERNAME                   = 'EMPTY_USERNAME'
    ERROR_EMPTY_PASSWORD                   = 'EMPTY_PASSWORD'
    ERROR_EMPTY_FIELDS                     = 'EMPTY_FIELDS'
    SUCCESS_USERNAME_PASSWORD_LENGTH       = 'GOOD_USERNAME_&_PASSWORD_LENGTH'
    SUCCESS_FIELDS_FILLED                  = 'ALL_FIELDS_FILLED'
    SUCCESS                                = 'SUCCESS'

    # result codes for LoginHandler
    ERROR_INVALID_USERNAME_OR_PASSWORD     = 'INVALID_USERNAME_OR_PASSWORD'
    NO_TOKEN                               = 'NO_TOKEN'

    # status return codes for index
    HTTP_200_OK                            = 200
    SUCCESS_USER_SIGN_UP                   = 201
    ERROR_USER_SIGN_UP                     = 202
