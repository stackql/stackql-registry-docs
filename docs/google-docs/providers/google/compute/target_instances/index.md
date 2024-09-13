
---
title: target_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - target_instances
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

Creates, updates, deletes or gets an <code>target_instance</code> resource or lists <code>target_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.target_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="instance" /> | `string` | A URL to the virtual machine instance that handles traffic for this target instance. When creating a target instance, you can provide the fully-qualified URL or a valid partial URL to the desired virtual machine. For example, the following are all valid URLs: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance - zones/zone/instances/instance  |
| <CopyableCode code="kind" /> | `string` | [Output Only] The type of the resource. Always compute#targetInstance for target instances. |
| <CopyableCode code="natPolicy" /> | `string` | Must have a value of NO_NAT. Protocol forwarding delivers packets while preserving the destination IP address of the forwarding rule referencing the target instance. |
| <CopyableCode code="network" /> | `string` | The URL of the network this target instance uses to forward traffic. If not specified, the traffic will be forwarded to the network that the default network interface belongs to. |
| <CopyableCode code="securityPolicy" /> | `string` | [Output Only] The resource URL for the security policy associated with this target instance. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="zone" /> | `string` | [Output Only] URL of the zone where the target instance resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of target instances. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, targetInstance, zone" /> | Returns the specified TargetInstance resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, zone" /> | Retrieves a list of TargetInstance resources available to the specified project and zone. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, zone" /> | Creates a TargetInstance resource in the specified project and zone using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, targetInstance, zone" /> | Deletes the specified TargetInstance resource. |
| <CopyableCode code="set_security_policy" /> | `EXEC` | <CopyableCode code="project, targetInstance, zone" /> | Sets the Google Cloud Armor security policy for the specified target instance. For more information, see Google Cloud Armor Overview |

## `SELECT` examples

Retrieves an aggregated list of target instances. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
creationTimestamp,
instance,
kind,
natPolicy,
network,
securityPolicy,
selfLink,
zone
FROM google.compute.target_instances
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>target_instances</code> resource.

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
INSERT INTO google.compute.target_instances (
project,
zone,
kind,
id,
creationTimestamp,
name,
description,
zone,
natPolicy,
instance,
selfLink,
network,
securityPolicy
)
SELECT 
'{{ project }}',
'{{ zone }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ zone }}',
'{{ natPolicy }}',
'{{ instance }}',
'{{ selfLink }}',
'{{ network }}',
'{{ securityPolicy }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: id
        value: '{{ id }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: zone
        value: '{{ zone }}'
      - name: natPolicy
        value: '{{ natPolicy }}'
      - name: instance
        value: '{{ instance }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: network
        value: '{{ network }}'
      - name: securityPolicy
        value: '{{ securityPolicy }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified target_instance resource.

```sql
DELETE FROM google.compute.target_instances
WHERE project = '{{ project }}'
AND targetInstance = '{{ targetInstance }}'
AND zone = '{{ zone }}';
```
