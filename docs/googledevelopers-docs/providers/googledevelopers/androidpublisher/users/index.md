---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - androidpublisher
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token to pass to subsequent calls in order to retrieve subsequent results. This will not be set if there are no more results to return. |
| `users` | `array` | The resulting users. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `developersId` | Lists all users with access to a developer account. |
| `create` | `INSERT` | `developersId` | Grant access for a user to the given developer account. |
| `delete` | `DELETE` | `developersId, usersId` | Removes all access for the user to the given developer account. |
| `patch` | `EXEC` | `developersId, usersId` | Updates access for the user to the developer account. |
