---
title: autokey_config
hide_title: false
hide_table_of_contents: false
keywords:
  - autokey_config
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

Creates, updates, deletes, gets or lists a <code>autokey_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autokey_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudkms.autokey_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the AutokeyConfig resource, e.g. `folders/{FOLDER_NUMBER}/autokeyConfig`. |
| <CopyableCode code="keyProject" /> | `string` | Optional. Name of the key project, e.g. `projects/{PROJECT_ID}` or `projects/{PROJECT_NUMBER}`, where Cloud KMS Autokey will provision a new CryptoKey when a KeyHandle is created. On UpdateAutokeyConfig, the caller will require `cloudkms.cryptoKeys.setIamPolicy` permission on this key project. Once configured, for Cloud KMS Autokey to function properly, this key project must have the Cloud KMS API activated and the Cloud KMS Service Agent for this key project must be granted the `cloudkms.admin` role (or pertinent permissions). A request with an empty key project field will clear the configuration. |
| <CopyableCode code="state" /> | `string` | Output only. The state for the AutokeyConfig. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_autokey_config" /> | `SELECT` | <CopyableCode code="foldersId" /> | Returns the AutokeyConfig for a folder. |
| <CopyableCode code="update_autokey_config" /> | `UPDATE` | <CopyableCode code="foldersId" /> | Updates the AutokeyConfig for a folder. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A KeyHandle creation in the folder's descendant projects will use this configuration to determine where to create the resulting CryptoKey. |

## `SELECT` examples

Returns the AutokeyConfig for a folder.

```sql
SELECT
name,
keyProject,
state
FROM google.cloudkms.autokey_config
WHERE foldersId = '{{ foldersId }}';
```

## `UPDATE` example

Updates a <code>autokey_config</code> resource.

```sql
/*+ update */
UPDATE google.cloudkms.autokey_config
SET 
name = '{{ name }}',
keyProject = '{{ keyProject }}'
WHERE 
foldersId = '{{ foldersId }}';
```
