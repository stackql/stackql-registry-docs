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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>crypto_keys_protected_resources_summary</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crypto_keys_protected_resources_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.kmsinventory.crypto_keys_protected_resources_summary" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The full name of the ProtectedResourcesSummary resource. Example: projects/test-project/locations/us/keyRings/test-keyring/cryptoKeys/test-key/protectedResourcesSummary |
| <CopyableCode code="cloudProducts" /> | `object` | The number of resources protected by the key grouped by Cloud product. |
| <CopyableCode code="locations" /> | `object` | The number of resources protected by the key grouped by region. |
| <CopyableCode code="projectCount" /> | `integer` | The number of distinct Cloud projects in the same Cloud organization as the key that have resources protected by the key. |
| <CopyableCode code="resourceCount" /> | `string` | The total number of protected resources in the same Cloud organization as the key. |
| <CopyableCode code="resourceTypes" /> | `object` | The number of resources protected by the key grouped by resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_protected_resources_summary" /> | `SELECT` | <CopyableCode code="cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Returns aggregate information about the resources protected by the given Cloud KMS CryptoKey. Only resources within the same Cloud organization as the key will be returned. The project that holds the key must be part of an organization in order for this call to succeed. |

## `SELECT` examples

Returns aggregate information about the resources protected by the given Cloud KMS CryptoKey. Only resources within the same Cloud organization as the key will be returned. The project that holds the key must be part of an organization in order for this call to succeed.

```sql
SELECT
name,
cloudProducts,
locations,
projectCount,
resourceCount,
resourceTypes
FROM google.kmsinventory.crypto_keys_protected_resources_summary
WHERE cryptoKeysId = '{{ cryptoKeysId }}'
AND keyRingsId = '{{ keyRingsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
