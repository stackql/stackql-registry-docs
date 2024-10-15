---
title: assets_encryption_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - assets_encryption_keys
  - media_services
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

Creates, updates, deletes, gets or lists a <code>assets_encryption_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets_encryption_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.assets_encryption_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="assetFileEncryptionMetadata" /> | `array` | Asset File encryption metadata. |
| <CopyableCode code="key" /> | `string` | The Asset File storage encryption key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, assetName, resourceGroupName, subscriptionId" /> | Gets the Asset storage encryption keys used to decrypt content created by version 2 of the Media Services API |

## `SELECT` examples

Gets the Asset storage encryption keys used to decrypt content created by version 2 of the Media Services API


```sql
SELECT
assetFileEncryptionMetadata,
key
FROM azure.media_services.assets_encryption_keys
WHERE accountName = '{{ accountName }}'
AND assetName = '{{ assetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```