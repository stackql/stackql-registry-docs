---
title: crypto_keys_primary_version
hide_title: false
hide_table_of_contents: false
keywords:
  - crypto_keys_primary_version
  - cloudkms
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

Creates, updates, deletes or gets an <code>crypto_keys_primary_version</code> resource or lists <code>crypto_keys_primary_version</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crypto_keys_primary_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudkms.crypto_keys_primary_version" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update_primary_version" /> | `UPDATE` | <CopyableCode code="cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Update the version of a CryptoKey that will be used in Encrypt. Returns an error if called on a key whose purpose is not ENCRYPT_DECRYPT. |

## `UPDATE` example

Updates a crypto_keys_primary_version only if the necessary resources are available.

```sql
UPDATE google.cloudkms.crypto_keys_primary_version
SET 
cryptoKeyVersionId = '{{ cryptoKeyVersionId }}'
WHERE 
cryptoKeysId = '{{ cryptoKeysId }}'
AND keyRingsId = '{{ keyRingsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
