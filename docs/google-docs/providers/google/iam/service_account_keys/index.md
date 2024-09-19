---
title: service_account_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - service_account_keys
  - iam
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

Creates, updates, deletes, gets or lists a <code>service_account_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_account_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.service_account_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the service account key in the following format `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}`. |
| <CopyableCode code="disableReason" /> | `string` | Output only. optional. If the key is disabled, it may have a DisableReason describing why it was disabled. |
| <CopyableCode code="disabled" /> | `boolean` | The key status. |
| <CopyableCode code="extendedStatus" /> | `array` | Output only. Extended Status provides permanent information about a service account key. For example, if this key was detected as exposed or compromised, that information will remain for the lifetime of the key in the extended_status. |
| <CopyableCode code="keyAlgorithm" /> | `string` | Specifies the algorithm (and possibly key size) for the key. |
| <CopyableCode code="keyOrigin" /> | `string` | The key origin. |
| <CopyableCode code="keyType" /> | `string` | The key type. |
| <CopyableCode code="privateKeyData" /> | `string` | The private key data. Only provided in `CreateServiceAccountKey` responses. Make sure to keep the private key data secure because it allows for the assertion of the service account identity. When base64 decoded, the private key data can be used to authenticate with Google API client libraries and with gcloud auth activate-service-account. |
| <CopyableCode code="privateKeyType" /> | `string` | The output format for the private key. Only provided in `CreateServiceAccountKey` responses, not in `GetServiceAccountKey` or `ListServiceAccountKey` responses. Google never exposes system-managed private keys, and never retains user-managed private keys. |
| <CopyableCode code="publicKeyData" /> | `string` | The public key data. Only provided in `GetServiceAccountKey` responses. |
| <CopyableCode code="validAfterTime" /> | `string` | The key can be used after this timestamp. |
| <CopyableCode code="validBeforeTime" /> | `string` | The key can be used before this timestamp. For system-managed key pairs, this timestamp is the end time for the private key signing operation. The public key could still be used for verification for a few hours after this time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keysId, projectsId, serviceAccountsId" /> | Gets a ServiceAccountKey. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId, serviceAccountsId" /> | Lists every ServiceAccountKey for a service account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId, serviceAccountsId" /> | Creates a ServiceAccountKey. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keysId, projectsId, serviceAccountsId" /> | Deletes a ServiceAccountKey. Deleting a service account key does not revoke short-lived credentials that have been issued based on the service account key. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="keysId, projectsId, serviceAccountsId" /> | Disable a ServiceAccountKey. A disabled service account key can be re-enabled with EnableServiceAccountKey. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="keysId, projectsId, serviceAccountsId" /> | Enable a ServiceAccountKey. |
| <CopyableCode code="upload" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | Uploads the public key portion of a key pair that you manage, and associates the public key with a ServiceAccount. After you upload the public key, you can use the private key from the key pair as a service account key. |

## `SELECT` examples

Lists every ServiceAccountKey for a service account.

```sql
SELECT
name,
disableReason,
disabled,
extendedStatus,
keyAlgorithm,
keyOrigin,
keyType,
privateKeyData,
privateKeyType,
publicKeyData,
validAfterTime,
validBeforeTime
FROM google.iam.service_account_keys
WHERE projectsId = '{{ projectsId }}'
AND serviceAccountsId = '{{ serviceAccountsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_account_keys</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.iam.service_account_keys (
projectsId,
serviceAccountsId,
privateKeyType,
keyAlgorithm
)
SELECT 
'{{ projectsId }}',
'{{ serviceAccountsId }}',
'{{ privateKeyType }}',
'{{ keyAlgorithm }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: privateKeyType
      value: string
    - name: keyAlgorithm
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>service_account_keys</code> resource.

```sql
/*+ delete */
DELETE FROM google.iam.service_account_keys
WHERE keysId = '{{ keysId }}'
AND projectsId = '{{ projectsId }}'
AND serviceAccountsId = '{{ serviceAccountsId }}';
```
