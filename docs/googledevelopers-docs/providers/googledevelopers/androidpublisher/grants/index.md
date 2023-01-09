---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
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
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.grants</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `create` | `INSERT` | `developersId, usersId` | Grant access for a user to the given package. |
| `delete` | `DELETE` | `developersId, grantsId, usersId` | Removes all access for the user to the given package or developer account. |
| `patch` | `EXEC` | `developersId, grantsId, usersId` | Updates access for the user to the given package. |
