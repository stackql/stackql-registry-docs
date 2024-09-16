---
title: endpoint_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_attachments
  - apigee
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

Creates, updates, deletes, gets or lists a <code>endpoint_attachments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.endpoint_attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the endpoint attachment. Use the following structure in your request: `organizations/{org}/endpointAttachments/{endpoint_attachment}` |
| <CopyableCode code="connectionState" /> | `string` | Output only. State of the endpoint attachment connection to the service attachment. |
| <CopyableCode code="host" /> | `string` | Output only. Host that can be used in either the HTTP target endpoint directly or as the host in target server. |
| <CopyableCode code="location" /> | `string` | Required. Location of the endpoint attachment. |
| <CopyableCode code="serviceAttachment" /> | `string` | Format: projects/*/regions/*/serviceAttachments/* |
| <CopyableCode code="state" /> | `string` | Output only. State of the endpoint attachment. Values other than `ACTIVE` mean the resource is not ready to use. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_endpoint_attachments_get" /> | `SELECT` | <CopyableCode code="endpointAttachmentsId, organizationsId" /> | Gets the endpoint attachment. |
| <CopyableCode code="organizations_endpoint_attachments_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists the endpoint attachments in an organization. |
| <CopyableCode code="organizations_endpoint_attachments_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates an endpoint attachment. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_endpoint_attachments_delete" /> | `DELETE` | <CopyableCode code="endpointAttachmentsId, organizationsId" /> | Deletes an endpoint attachment. |

## `SELECT` examples

Lists the endpoint attachments in an organization.

```sql
SELECT
name,
connectionState,
host,
location,
serviceAttachment,
state
FROM google.apigee.endpoint_attachments
WHERE organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoint_attachments</code> resource.

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
INSERT INTO google.apigee.endpoint_attachments (
organizationsId,
name,
connectionState,
serviceAttachment,
location,
state,
host
)
SELECT 
'{{ organizationsId }}',
'{{ name }}',
'{{ connectionState }}',
'{{ serviceAttachment }}',
'{{ location }}',
'{{ state }}',
'{{ host }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: connectionState
      value: '{{ connectionState }}'
    - name: serviceAttachment
      value: '{{ serviceAttachment }}'
    - name: location
      value: '{{ location }}'
    - name: state
      value: '{{ state }}'
    - name: host
      value: '{{ host }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>endpoint_attachments</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.endpoint_attachments
WHERE endpointAttachmentsId = '{{ endpointAttachmentsId }}'
AND organizationsId = '{{ organizationsId }}';
```
