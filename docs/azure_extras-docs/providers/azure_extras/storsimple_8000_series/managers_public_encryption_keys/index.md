---
title: managers_public_encryption_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - managers_public_encryption_keys
  - storsimple_8000_series
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

Creates, updates, deletes, gets or lists a <code>managers_public_encryption_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managers_public_encryption_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.managers_public_encryption_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="encryptionAlgorithm" /> | `string` | The algorithm used to encrypt the "Value". |
| <CopyableCode code="value" /> | `string` | The value of the secret itself. If the secret is in plaintext or null then EncryptionAlgorithm will be none. |
| <CopyableCode code="valueCertificateThumbprint" /> | `string` | The thumbprint of the cert that was used to encrypt "Value". |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Returns the symmetric encrypted public encryption key of the manager. |

## `SELECT` examples

Returns the symmetric encrypted public encryption key of the manager.


```sql
SELECT
encryptionAlgorithm,
value,
valueCertificateThumbprint
FROM azure_extras.storsimple_8000_series.managers_public_encryption_keys
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```