---
title: operations_discovery
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_discovery
  - resource_mover
  - azure    
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
<tr><td><b>Name</b></td><td><code>operations_discovery</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_mover.operations_discovery</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Gets or sets Name of the API.<br />The name of the operation being performed on this particular object. It should<br />match the action name that appears in RBAC / the event service.<br />Examples of operations include:<br />* Microsoft.Compute/virtualMachine/capture/action<br />* Microsoft.Compute/virtualMachine/restart/action<br />* Microsoft.Compute/virtualMachine/write<br />* Microsoft.Compute/virtualMachine/read<br />* Microsoft.Compute/virtualMachine/delete<br />Each action should include, in order:<br />(1) Resource Provider Namespace<br />(2) Type hierarchy for which the action applies (e.g. server/databases for a SQL<br />Azure database)<br />(3) Read, Write, Action or Delete indicating which type applies. If it is a PUT/PATCH<br />on a collection or named value, Write should be used.<br />If it is a GET, Read should be used. If it is a DELETE, Delete should be used. If it<br />is a POST, Action should be used.<br />As a note: all resource providers would need to include the "&#123;Resource Provider<br />Namespace&#125;/register/action" operation in their response.<br />This API is used to register for their service, and should include details about the<br />operation (e.g. a localized name for the resource provider + any special<br />considerations like PII release). |
| `display` | `object` | Contains the localized display information for this particular operation / action. These<br />value will be used by several clients for<br />(1) custom role definitions for RBAC;<br />(2) complex query filters for the event service; and<br />(3) audit history / records for management operations. |
| `isDataAction` | `boolean` | Indicates whether the operation is a data action |
| `origin` | `string` | Gets or sets Origin.<br />The intended executor of the operation; governs the display of the operation in the<br />RBAC UX and the audit logs UX.<br />Default value is "user,system". |
| `properties` | `object` | ClientDiscovery properties. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version` |
| `_get` | `EXEC` | `api-version` |
