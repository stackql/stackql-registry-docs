---
title: identity_aware_proxy_clients
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_aware_proxy_clients
  - iap
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

Creates, updates, deletes, gets or lists a <code>identity_aware_proxy_clients</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_aware_proxy_clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iap.identity_aware_proxy_clients" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Unique identifier of the OAuth client. |
| <CopyableCode code="displayName" /> | `string` | Human-friendly name given to the OAuth client. |
| <CopyableCode code="secret" /> | `string` | Output only. Client secret of the OAuth client. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="brandsId, identityAwareProxyClientsId, projectsId" /> | Retrieves an Identity Aware Proxy (IAP) OAuth client. Requires that the client is owned by IAP. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="brandsId, projectsId" /> | Lists the existing clients for the brand. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="brandsId, projectsId" /> | Creates an Identity Aware Proxy (IAP) OAuth client. The client is owned by IAP. Requires that the brand for the project exists and that it is set for internal-only use. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="brandsId, identityAwareProxyClientsId, projectsId" /> | Deletes an Identity Aware Proxy (IAP) OAuth client. Useful for removing obsolete clients, managing the number of clients in a given project, and cleaning up after tests. Requires that the client is owned by IAP. |
| <CopyableCode code="reset_secret" /> | `EXEC` | <CopyableCode code="brandsId, identityAwareProxyClientsId, projectsId" /> | Resets an Identity Aware Proxy (IAP) OAuth client secret. Useful if the secret was compromised. Requires that the client is owned by IAP. |

## `SELECT` examples

Lists the existing clients for the brand.

```sql
SELECT
name,
displayName,
secret
FROM google.iap.identity_aware_proxy_clients
WHERE brandsId = '{{ brandsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>identity_aware_proxy_clients</code> resource.

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
INSERT INTO google.iap.identity_aware_proxy_clients (
brandsId,
projectsId,
name,
secret,
displayName
)
SELECT 
'{{ brandsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ secret }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: secret
        value: '{{ secret }}'
      - name: displayName
        value: '{{ displayName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>identity_aware_proxy_clients</code> resource.

```sql
/*+ delete */
DELETE FROM google.iap.identity_aware_proxy_clients
WHERE brandsId = '{{ brandsId }}'
AND identityAwareProxyClientsId = '{{ identityAwareProxyClientsId }}'
AND projectsId = '{{ projectsId }}';
```
