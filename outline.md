job:
    -title
    -location
    -job type
    -description
    -published at
    -vacancy
    -salary
    -catigory
    -experience
    -gender

    -apply job
    -post job

blog:
    -title
    -published at
    -creadted at
    -category
    -tags
    -author

    -search
    -comment
    -recent posts


home 
sign in
contact


relations:
    -one to many    [author - posts]    foreginkey
    -many to many   [ user - groups]    
    -one to one     [user - profile]