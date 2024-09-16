---
title: idp_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - idp_credentials
  - cloudidentity
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

Creates, updates, deletes, gets or lists a <code>idp_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>idp_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.idp_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the credential. |
| <CopyableCode code="dsaKeyInfo" /> | `object` | Information of a DSA public key. |
| <CopyableCode code="rsaKeyInfo" /> | `object` | Information of a RSA public key. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the `IdpCredential` was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="idpCredentialsId, inboundSamlSsoProfilesId" /> | Gets an IdpCredential. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="inboundSamlSsoProfilesId" /> | Returns a list of IdpCredentials in an InboundSamlSsoProfile. |
| <CopyableCode code="add" /> | `INSERT` | <CopyableCode code="inboundSamlSsoProfilesId" /> | Adds an IdpCredential. Up to 2 credentials are allowed. When the target customer has enabled [Multi-party approval for sensitive actions](https://support.google.com/a/answer/13790448), the `Operation` in the response will have `"done": false`, it will not have a response, and the metadata will have `"state": "awaiting-multi-party-approval"`. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="idpCredentialsId, inboundSamlSsoProfilesId" /> | Deletes an IdpCredential. |

## `SELECT` examples

Returns a list of IdpCredentials in an InboundSamlSsoProfile.

```sql
SELECT
name,
dsaKeyInfo,
rsaKeyInfo,
updateTime
FROM google.cloudidentity.idp_credentials
WHERE inboundSamlSsoProfilesId = '{{ inboundSamlSsoProfilesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>idp_credentials</code> resource.

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
INSERT INTO google.cloudidentity.idp_credentials (
inboundSamlSsoProfilesId,
pemData
)
SELECT 
'{{ inboundSamlSsoProfilesId }}',
'{{ pemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: pemData
      value: '{{ pemData }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>idp_credentials</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudidentity.idp_credentials
WHERE idpCredentialsId = '{{ idpCredentialsId }}'
AND inboundSamlSsoProfilesId = '{{ inboundSamlSsoProfilesId }}';
```
