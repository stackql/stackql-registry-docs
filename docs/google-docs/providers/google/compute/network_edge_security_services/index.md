---
title: network_edge_security_services
hide_title: false
hide_table_of_contents: false
keywords:
  - network_edge_security_services
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

Creates, updates, deletes, gets or lists a <code>network_edge_security_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_edge_security_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.network_edge_security_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a NetworkEdgeSecurityService. An up-to-date fingerprint must be provided in order to update the NetworkEdgeSecurityService, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a NetworkEdgeSecurityService. |
| <CopyableCode code="kind" /> | `string` | [Output only] Type of the resource. Always compute#networkEdgeSecurityService for NetworkEdgeSecurityServices |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the resource resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="securityPolicy" /> | `string` | The resource URL for the network edge security service associated with this network edge security service. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="selfLinkWithId" /> | `string` | [Output Only] Server-defined URL for this resource with the resource id. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of all NetworkEdgeSecurityService resources available to the specified project. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkEdgeSecurityService, project, region" /> | Gets a specified NetworkEdgeSecurityService. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a new service in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkEdgeSecurityService, project, region" /> | Deletes the specified service. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="networkEdgeSecurityService, project, region" /> | Patches the specified policy with the data included in the request. |

## `SELECT` examples

Retrieves the list of all NetworkEdgeSecurityService resources available to the specified project. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
creationTimestamp,
fingerprint,
kind,
region,
securityPolicy,
selfLink,
selfLinkWithId
FROM google.compute.network_edge_security_services
WHERE project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_edge_security_services</code> resource.

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
INSERT INTO google.compute.network_edge_security_services (
project,
region,
name,
description,
region,
fingerprint,
securityPolicy
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ description }}',
'{{ region }}',
'{{ fingerprint }}',
'{{ securityPolicy }}'
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
    - name: selfLink
      value: string
    - name: selfLinkWithId
      value: string
    - name: region
      value: string
    - name: fingerprint
      value: string
    - name: securityPolicy
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_edge_security_services</code> resource.

```sql
/*+ update */
UPDATE google.compute.network_edge_security_services
SET 
name = '{{ name }}',
description = '{{ description }}',
region = '{{ region }}',
fingerprint = '{{ fingerprint }}',
securityPolicy = '{{ securityPolicy }}'
WHERE 
networkEdgeSecurityService = '{{ networkEdgeSecurityService }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified <code>network_edge_security_services</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.network_edge_security_services
WHERE networkEdgeSecurityService = '{{ networkEdgeSecurityService }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
