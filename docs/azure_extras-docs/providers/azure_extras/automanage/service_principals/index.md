---
title: service_principals
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principals
  - automanage
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
<tr><td><b>Name</b></td><td><code>service_principals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automanage.service_principals</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | The Service Principal properties for the subscription. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ServicePrincipals_ListBySubscription` | `SELECT` | `subscriptionId` |
| `ServicePrincipals_Get` | `EXEC` | `subscriptionId` |
