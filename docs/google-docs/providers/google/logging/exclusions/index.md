---
title: exclusions
hide_title: false
hide_table_of_contents: false
keywords:
  - exclusions
  - logging
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>exclusions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.exclusions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. A client-assigned identifier, such as "load-balancer-exclusion". Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods. First character has to be alphanumeric. |
| `description` | `string` | Optional. A description of this exclusion. |
| `disabled` | `boolean` | Optional. If set to True, then this exclusion is disabled and it does not exclude any log entries. You can update an exclusion to change the value of this field. |
| `filter` | `string` | Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries) that matches the log entries to be excluded. By using the sample function (https://cloud.google.com/logging/docs/view/advanced-queries#sample), you can exclude less than 100% of the matching log entries.For example, the following query matches 99% of low-severity log entries from Google Cloud Storage buckets:resource.type=gcs_bucket severity&lt;ERROR sample(insertId, 0.99) |
| `updateTime` | `string` | Output only. The last update timestamp of the exclusion.This field may not be present for older exclusions. |
| `createTime` | `string` | Output only. The creation timestamp of the exclusion.This field may not be present for older exclusions. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billingAccounts_exclusions_get` | `SELECT` | `billingAccountsId, exclusionsId` | Gets the description of an exclusion in the _Default sink. |
| `billingAccounts_exclusions_list` | `SELECT` | `billingAccountsId` | Lists all the exclusions on the _Default sink in a parent resource. |
| `folders_exclusions_get` | `SELECT` | `exclusionsId, foldersId` | Gets the description of an exclusion in the _Default sink. |
| `folders_exclusions_list` | `SELECT` | `foldersId` | Lists all the exclusions on the _Default sink in a parent resource. |
| `list` | `SELECT` | `parent` | Lists all the exclusions on the _Default sink in a parent resource. |
| `organizations_exclusions_get` | `SELECT` | `exclusionsId, organizationsId` | Gets the description of an exclusion in the _Default sink. |
| `organizations_exclusions_list` | `SELECT` | `organizationsId` | Lists all the exclusions on the _Default sink in a parent resource. |
| `projects_exclusions_get` | `SELECT` | `exclusionsId, projectsId` | Gets the description of an exclusion in the _Default sink. |
| `projects_exclusions_list` | `SELECT` | `projectsId` | Lists all the exclusions on the _Default sink in a parent resource. |
| `billingAccounts_exclusions_create` | `INSERT` | `billingAccountsId` | Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource. |
| `create` | `INSERT` | `parent` | Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource. |
| `folders_exclusions_create` | `INSERT` | `foldersId` | Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource. |
| `organizations_exclusions_create` | `INSERT` | `organizationsId` | Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource. |
| `projects_exclusions_create` | `INSERT` | `projectsId` | Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource. |
| `billingAccounts_exclusions_delete` | `DELETE` | `billingAccountsId, exclusionsId` | Deletes an exclusion in the _Default sink. |
| `folders_exclusions_delete` | `DELETE` | `exclusionsId, foldersId` | Deletes an exclusion in the _Default sink. |
| `organizations_exclusions_delete` | `DELETE` | `exclusionsId, organizationsId` | Deletes an exclusion in the _Default sink. |
| `projects_exclusions_delete` | `DELETE` | `exclusionsId, projectsId` | Deletes an exclusion in the _Default sink. |
| `billingAccounts_exclusions_patch` | `EXEC` | `billingAccountsId, exclusionsId` | Changes one or more properties of an existing exclusion in the _Default sink. |
| `folders_exclusions_patch` | `EXEC` | `exclusionsId, foldersId` | Changes one or more properties of an existing exclusion in the _Default sink. |
| `organizations_exclusions_patch` | `EXEC` | `exclusionsId, organizationsId` | Changes one or more properties of an existing exclusion in the _Default sink. |
| `projects_exclusions_patch` | `EXEC` | `exclusionsId, projectsId` | Changes one or more properties of an existing exclusion in the _Default sink. |
