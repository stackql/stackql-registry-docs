---
title: server_tls_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - server_tls_policies
  - networksecurity
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

Creates, updates, deletes, gets or lists a <code>server_tls_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_tls_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.server_tls_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the ServerTlsPolicy resource. It matches the pattern `projects/*/locations/{location}/serverTlsPolicies/{server_tls_policy}` |
| <CopyableCode code="description" /> | `string` | Free-text description of the resource. |
| <CopyableCode code="allowOpen" /> | `boolean` | This field applies only for Traffic Director policies. It is must be set to false for Application Load Balancer policies. Determines if server allows plaintext connections. If set to true, server allows plain text connections. By default, it is set to false. This setting is not exclusive of other encryption modes. For example, if `allow_open` and `mtls_policy` are set, server allows both plain text and mTLS connections. See documentation of other encryption modes to confirm compatibility. Consider using it if you wish to upgrade in place your deployment to TLS while having mixed TLS and non-TLS traffic reaching port :80. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="labels" /> | `object` | Set of label tags associated with the resource. |
| <CopyableCode code="mtlsPolicy" /> | `object` | Specification of the MTLSPolicy. |
| <CopyableCode code="serverCertificate" /> | `object` | Specification of certificate provider. Defines the mechanism to obtain the certificate and private key for peer to peer authentication. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_server_tls_policies_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, serverTlsPoliciesId" /> | Gets details of a single ServerTlsPolicy. |
| <CopyableCode code="projects_locations_server_tls_policies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ServerTlsPolicies in a given project and location. |
| <CopyableCode code="projects_locations_server_tls_policies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ServerTlsPolicy in a given project and location. |
| <CopyableCode code="projects_locations_server_tls_policies_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, serverTlsPoliciesId" /> | Deletes a single ServerTlsPolicy. |
| <CopyableCode code="projects_locations_server_tls_policies_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, serverTlsPoliciesId" /> | Updates the parameters of a single ServerTlsPolicy. |

## `SELECT` examples

Lists ServerTlsPolicies in a given project and location.

```sql
SELECT
name,
description,
allowOpen,
createTime,
labels,
mtlsPolicy,
serverCertificate,
updateTime
FROM google.networksecurity.server_tls_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_tls_policies</code> resource.

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
INSERT INTO google.networksecurity.server_tls_policies (
locationsId,
projectsId,
name,
description,
createTime,
updateTime,
labels,
allowOpen,
serverCertificate,
mtlsPolicy
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
true|false,
'{{ serverCertificate }}',
'{{ mtlsPolicy }}'
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
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: allowOpen
        value: '{{ allowOpen }}'
      - name: serverCertificate
        value: '{{ serverCertificate }}'
      - name: mtlsPolicy
        value: '{{ mtlsPolicy }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>server_tls_policies</code> resource.

```sql
/*+ update */
UPDATE google.networksecurity.server_tls_policies
SET 
name = '{{ name }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
allowOpen = true|false,
serverCertificate = '{{ serverCertificate }}',
mtlsPolicy = '{{ mtlsPolicy }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND serverTlsPoliciesId = '{{ serverTlsPoliciesId }}';
```

## `DELETE` example

Deletes the specified <code>server_tls_policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.networksecurity.server_tls_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND serverTlsPoliciesId = '{{ serverTlsPoliciesId }}';
```
