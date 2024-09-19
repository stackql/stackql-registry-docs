---
title: node_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - node_templates
  - compute
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

Creates, updates, deletes, gets or lists a <code>node_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.node_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="accelerators" /> | `array` |  |
| <CopyableCode code="cpuOvercommitType" /> | `string` | CPU overcommit. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="disks" /> | `array` |  |
| <CopyableCode code="kind" /> | `string` | [Output Only] The type of the resource. Always compute#nodeTemplate for node templates. |
| <CopyableCode code="nodeAffinityLabels" /> | `object` | Labels to use for node affinity, which will be used in instance scheduling. |
| <CopyableCode code="nodeType" /> | `string` | The node type to use for nodes group that are created from this template. |
| <CopyableCode code="nodeTypeFlexibility" /> | `object` |  |
| <CopyableCode code="region" /> | `string` | [Output Only] The name of the region where the node template resides, such as us-central1. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="serverBinding" /> | `object` |  |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of the node template. One of the following values: CREATING, READY, and DELETING. |
| <CopyableCode code="statusMessage" /> | `string` | [Output Only] An optional, human-readable explanation of the status. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of node templates. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="nodeTemplate, project, region" /> | Returns the specified node template. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of node templates available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a NodeTemplate resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="nodeTemplate, project, region" /> | Deletes the specified NodeTemplate resource. |

## `SELECT` examples

Retrieves an aggregated list of node templates. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
accelerators,
cpuOvercommitType,
creationTimestamp,
disks,
kind,
nodeAffinityLabels,
nodeType,
nodeTypeFlexibility,
region,
selfLink,
serverBinding,
status,
statusMessage
FROM google.compute.node_templates
WHERE project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>node_templates</code> resource.

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
INSERT INTO google.compute.node_templates (
project,
region,
name,
description,
nodeType,
nodeAffinityLabels,
status,
statusMessage,
region,
nodeTypeFlexibility,
serverBinding,
disks,
accelerators,
cpuOvercommitType
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ description }}',
'{{ nodeType }}',
'{{ nodeAffinityLabels }}',
'{{ status }}',
'{{ statusMessage }}',
'{{ region }}',
'{{ nodeTypeFlexibility }}',
'{{ serverBinding }}',
'{{ disks }}',
'{{ accelerators }}',
'{{ cpuOvercommitType }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: id
      value: string
    - name: creationTimestamp
      value: string
    - name: name
      value: string
    - name: description
      value: string
    - name: nodeType
      value: string
    - name: nodeAffinityLabels
      value: object
    - name: status
      value: string
    - name: statusMessage
      value: string
    - name: region
      value: string
    - name: selfLink
      value: string
    - name: nodeTypeFlexibility
      value:
        - name: cpus
          value: string
        - name: memory
          value: string
        - name: localSsd
          value: string
    - name: serverBinding
      value:
        - name: type
          value: string
    - name: disks
      value:
        - - name: diskType
            value: string
          - name: diskSizeGb
            value: integer
          - name: diskCount
            value: integer
    - name: accelerators
      value:
        - - name: acceleratorType
            value: string
          - name: acceleratorCount
            value: integer
    - name: cpuOvercommitType
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>node_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.node_templates
WHERE nodeTemplate = '{{ nodeTemplate }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
