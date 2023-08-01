---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.features</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the feature. |
| `etags` | `string` | ETag of the resource. |
| `kind` | `string` | Kind of resource this is. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customer, featureKey` | Retrieves a feature. |
| `list` | `SELECT` | `customer` | Retrieves a list of features for an account. |
| `insert` | `INSERT` | `customer` | Inserts a feature. |
| `delete` | `DELETE` | `customer, featureKey` | Deletes a feature. |
| `_list` | `EXEC` | `customer` | Retrieves a list of features for an account. |
| `patch` | `EXEC` | `customer, featureKey` | Patches a feature. |
| `rename` | `EXEC` | `customer, oldName` | Renames a feature. |
| `update` | `EXEC` | `customer, featureKey` | Updates a feature. |
