---
title: packages
hide_title: false
hide_table_of_contents: false
keywords:
  - packages
  - test_base
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties of the Test Base Package. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | Resource Etag. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Packages_Get` | `SELECT` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets a Test Base Package. |
| `Packages_ListByTestBaseAccount` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the packages under a Test Base Account. |
| `Packages_Create` | `INSERT` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Create or replace (overwrite/recreate, with potential downtime) a Test Base Package. |
| `Packages_Delete` | `DELETE` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Deletes a Test Base Package. |
| `Packages_GetDownloadURL` | `EXEC` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets the download URL of a package. |
| `Packages_HardDelete` | `EXEC` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Hard Delete a Test Base Package. |
| `Packages_RunTest` | `EXEC` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName, data__osName, data__testType` | Trigger a test run on the package. |
| `Packages_Update` | `EXEC` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Update an existing Test Base Package. |
