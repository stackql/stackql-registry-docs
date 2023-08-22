---
title: crypto_keys_protected_resources_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - crypto_keys_protected_resources_summary
  - kmsinventory
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crypto_keys_protected_resources_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.kmsinventory.crypto_keys_protected_resources_summary</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The full name of the ProtectedResourcesSummary resource. Example: projects/test-project/locations/us/keyRings/test-keyring/cryptoKeys/test-key/protectedResourcesSummary |
| `projectCount` | `integer` | The number of distinct Cloud projects in the same Cloud organization as the key that have resources protected by the key. |
| `resourceCount` | `string` | The total number of protected resources in the same Cloud organization as the key. |
| `resourceTypes` | `object` | The number of resources protected by the key grouped by resource type. |
| `cloudProducts` | `object` | The number of resources protected by the key grouped by Cloud product. |
| `locations` | `object` | The number of resources protected by the key grouped by region. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_protected_resources_summary` | `SELECT` | `cryptoKeysId, keyRingsId, locationsId, projectsId` |
