---
title: dns_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_authorizations
  - certificatemanager
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

Creates, updates, deletes, gets or lists a <code>dns_authorizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dns_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.certificatemanager.dns_authorizations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. A user-defined name of the dns authorization. DnsAuthorization names must be unique globally and match pattern `projects/*/locations/*/dnsAuthorizations/*`. |
| <CopyableCode code="description" /> | `string` | Optional. One or more paragraphs of text description of a DnsAuthorization. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of a DnsAuthorization. |
| <CopyableCode code="dnsResourceRecord" /> | `object` | The structure describing the DNS Resource Record that needs to be added to DNS configuration for the authorization to be usable by certificate. |
| <CopyableCode code="domain" /> | `string` | Required. Immutable. A domain that is being authorized. A DnsAuthorization resource covers a single domain and its wildcard, e.g. authorization for `example.com` can be used to issue certificates for `example.com` and `*.example.com`. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of labels associated with a DnsAuthorization. |
| <CopyableCode code="type" /> | `string` | Optional. Immutable. Type of DnsAuthorization. If unset during resource creation the following default will be used: - in location `global`: FIXED_RECORD, - in other locations: PER_PROJECT_RECORD. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of a DnsAuthorization. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsAuthorizationsId, locationsId, projectsId" /> | Gets details of a single DnsAuthorization. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DnsAuthorizations in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new DnsAuthorization in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsAuthorizationsId, locationsId, projectsId" /> | Deletes a single DnsAuthorization. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="dnsAuthorizationsId, locationsId, projectsId" /> | Updates a DnsAuthorization. |

## `SELECT` examples

Lists DnsAuthorizations in a given project and location.

```sql
SELECT
name,
description,
createTime,
dnsResourceRecord,
domain,
labels,
type,
updateTime
FROM google.certificatemanager.dns_authorizations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dns_authorizations</code> resource.

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
INSERT INTO google.certificatemanager.dns_authorizations (
locationsId,
projectsId,
name,
labels,
description,
domain,
type
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ labels }}',
'{{ description }}',
'{{ domain }}',
'{{ type }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
updateTime: string
labels: object
description: string
domain: string
dnsResourceRecord:
  name: string
  type: string
  data: string
type: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dns_authorizations</code> resource.

```sql
/*+ update */
UPDATE google.certificatemanager.dns_authorizations
SET 
name = '{{ name }}',
labels = '{{ labels }}',
description = '{{ description }}',
domain = '{{ domain }}',
type = '{{ type }}'
WHERE 
dnsAuthorizationsId = '{{ dnsAuthorizationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>dns_authorizations</code> resource.

```sql
/*+ delete */
DELETE FROM google.certificatemanager.dns_authorizations
WHERE dnsAuthorizationsId = '{{ dnsAuthorizationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
