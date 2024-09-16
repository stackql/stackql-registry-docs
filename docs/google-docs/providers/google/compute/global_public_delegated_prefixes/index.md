---
title: global_public_delegated_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - global_public_delegated_prefixes
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

Creates, updates, deletes, gets or lists a <code>global_public_delegated_prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_public_delegated_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.global_public_delegated_prefixes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource type. The server generates this identifier. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="allocatablePrefixLength" /> | `integer` | The allocatable prefix length supported by this public delegated prefix. This field is optional and cannot be set for prefixes in DELEGATION mode. It cannot be set for IPv4 prefixes either, and it always defaults to 32. |
| <CopyableCode code="byoipApiVersion" /> | `string` | [Output Only] The version of BYOIP API. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a new PublicDelegatedPrefix. An up-to-date fingerprint must be provided in order to update the PublicDelegatedPrefix, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a PublicDelegatedPrefix. |
| <CopyableCode code="ipCidrRange" /> | `string` | The IP address range, in CIDR format, represented by this public delegated prefix. |
| <CopyableCode code="isLiveMigration" /> | `boolean` | If true, the prefix will be live migrated. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#publicDelegatedPrefix for public delegated prefixes. |
| <CopyableCode code="mode" /> | `string` | The public delegated prefix mode for IPv6 only. |
| <CopyableCode code="parentPrefix" /> | `string` | The URL of parent prefix. Either PublicAdvertisedPrefix or PublicDelegatedPrefix. |
| <CopyableCode code="publicDelegatedSubPrefixs" /> | `array` | The list of sub public delegated prefixes that exist for this public delegated prefix. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the public delegated prefix resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of the public delegated prefix, which can be one of following values: - `INITIALIZING` The public delegated prefix is being initialized and addresses cannot be created yet. - `READY_TO_ANNOUNCE` The public delegated prefix is a live migration prefix and is active. - `ANNOUNCED` The public delegated prefix is active. - `DELETING` The public delegated prefix is being deprovsioned.  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, publicDelegatedPrefix" /> | Returns the specified global PublicDelegatedPrefix resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Lists the global PublicDelegatedPrefixes for a project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a global PublicDelegatedPrefix in the specified project using the parameters that are included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, publicDelegatedPrefix" /> | Deletes the specified global PublicDelegatedPrefix. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, publicDelegatedPrefix" /> | Patches the specified global PublicDelegatedPrefix resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |

## `SELECT` examples

Lists the global PublicDelegatedPrefixes for a project.

```sql
SELECT
id,
name,
description,
allocatablePrefixLength,
byoipApiVersion,
creationTimestamp,
fingerprint,
ipCidrRange,
isLiveMigration,
kind,
mode,
parentPrefix,
publicDelegatedSubPrefixs,
region,
selfLink,
status
FROM google.compute.global_public_delegated_prefixes
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>global_public_delegated_prefixes</code> resource.

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
INSERT INTO google.compute.global_public_delegated_prefixes (
project,
kind,
id,
creationTimestamp,
name,
description,
selfLink,
region,
ipCidrRange,
status,
parentPrefix,
publicDelegatedSubPrefixs,
isLiveMigration,
fingerprint,
mode,
allocatablePrefixLength,
byoipApiVersion
)
SELECT 
'{{ project }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ selfLink }}',
'{{ region }}',
'{{ ipCidrRange }}',
'{{ status }}',
'{{ parentPrefix }}',
'{{ publicDelegatedSubPrefixs }}',
true|false,
'{{ fingerprint }}',
'{{ mode }}',
'{{ allocatablePrefixLength }}',
'{{ byoipApiVersion }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
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
    - name: selfLink
      value: '{{ selfLink }}'
    - name: region
      value: '{{ region }}'
    - name: ipCidrRange
      value: '{{ ipCidrRange }}'
    - name: status
      value: '{{ status }}'
    - name: parentPrefix
      value: '{{ parentPrefix }}'
    - name: publicDelegatedSubPrefixs
      value: '{{ publicDelegatedSubPrefixs }}'
    - name: isLiveMigration
      value: '{{ isLiveMigration }}'
    - name: fingerprint
      value: '{{ fingerprint }}'
    - name: mode
      value: '{{ mode }}'
    - name: allocatablePrefixLength
      value: '{{ allocatablePrefixLength }}'
    - name: byoipApiVersion
      value: '{{ byoipApiVersion }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>global_public_delegated_prefixes</code> resource.

```sql
/*+ update */
UPDATE google.compute.global_public_delegated_prefixes
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
selfLink = '{{ selfLink }}',
region = '{{ region }}',
ipCidrRange = '{{ ipCidrRange }}',
status = '{{ status }}',
parentPrefix = '{{ parentPrefix }}',
publicDelegatedSubPrefixs = '{{ publicDelegatedSubPrefixs }}',
isLiveMigration = true|false,
fingerprint = '{{ fingerprint }}',
mode = '{{ mode }}',
allocatablePrefixLength = '{{ allocatablePrefixLength }}',
byoipApiVersion = '{{ byoipApiVersion }}'
WHERE 
project = '{{ project }}'
AND publicDelegatedPrefix = '{{ publicDelegatedPrefix }}';
```

## `DELETE` example

Deletes the specified <code>global_public_delegated_prefixes</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.global_public_delegated_prefixes
WHERE project = '{{ project }}'
AND publicDelegatedPrefix = '{{ publicDelegatedPrefix }}';
```
