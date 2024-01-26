---
title: certificate_object_local_rulestack
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_object_local_rulestack
  - paloaltonetworks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>certificate_object_local_rulestack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.paloaltonetworks.certificate_object_local_rulestack</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | certificate used for inbound and outbound decryption |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `localRulestackName, name, resourceGroupName, subscriptionId` | Get a CertificateObjectLocalRulestackResource |
| `list_by_local_rulestacks` | `SELECT` | `localRulestackName, resourceGroupName, subscriptionId` | List CertificateObjectLocalRulestackResource resources by LocalRulestacks |
| `create_or_update` | `INSERT` | `localRulestackName, name, resourceGroupName, subscriptionId, data__properties` | Create a CertificateObjectLocalRulestackResource |
| `delete` | `DELETE` | `localRulestackName, name, resourceGroupName, subscriptionId` | Delete a CertificateObjectLocalRulestackResource |
| `_list_by_local_rulestacks` | `EXEC` | `localRulestackName, resourceGroupName, subscriptionId` | List CertificateObjectLocalRulestackResource resources by LocalRulestacks |
