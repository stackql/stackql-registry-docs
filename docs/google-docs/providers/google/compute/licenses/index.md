
---
title: licenses
hide_title: false
hide_table_of_contents: false
keywords:
  - licenses
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

Creates, updates, deletes or gets an <code>license</code> resource or lists <code>licenses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.licenses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. The name must be 1-63 characters long and comply with RFC1035. |
| <CopyableCode code="description" /> | `string` | An optional textual description of the resource; provided by the client when the resource is created. |
| <CopyableCode code="chargesUseFee" /> | `boolean` | [Output Only] Deprecated. This field no longer reflects whether a license charges a usage fee. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of resource. Always compute#license for licenses. |
| <CopyableCode code="licenseCode" /> | `string` | [Output Only] The unique code used to attach this license to images, snapshots, and disks. |
| <CopyableCode code="resourceRequirements" /> | `object` |  |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="transferable" /> | `boolean` | If false, licenses will not be copied from the source resource when creating an image from a disk, disk from snapshot, or snapshot from disk. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="license, project" /> | Returns the specified License resource. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of licenses available in the specified project. This method does not get any licenses that belong to other projects, including licenses attached to publicly-available images, like Debian 9. If you want to get a list of publicly-available licenses, use this method to make a request to the respective image project, such as debian-cloud or windows-cloud. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.  |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Create a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="license, project" /> | Deletes the specified license. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.  |

## `SELECT` examples

Retrieves the list of licenses available in the specified project. This method does not get any licenses that belong to other projects, including licenses attached to publicly-available images, like Debian 9. If you want to get a list of publicly-available licenses, use this method to make a request to the respective image project, such as debian-cloud or windows-cloud. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images. 

```sql
SELECT
id,
name,
description,
chargesUseFee,
creationTimestamp,
kind,
licenseCode,
resourceRequirements,
selfLink,
transferable
FROM google.compute.licenses
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>licenses</code> resource.

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
INSERT INTO google.compute.licenses (
project,
kind,
name,
chargesUseFee,
id,
licenseCode,
creationTimestamp,
description,
transferable,
selfLink,
resourceRequirements
)
SELECT 
'{{ project }}',
'{{ kind }}',
'{{ name }}',
true|false,
'{{ id }}',
'{{ licenseCode }}',
'{{ creationTimestamp }}',
'{{ description }}',
true|false,
'{{ selfLink }}',
'{{ resourceRequirements }}'
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
      - name: name
        value: '{{ name }}'
      - name: chargesUseFee
        value: '{{ chargesUseFee }}'
      - name: id
        value: '{{ id }}'
      - name: licenseCode
        value: '{{ licenseCode }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: description
        value: '{{ description }}'
      - name: transferable
        value: '{{ transferable }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: resourceRequirements
        value: '{{ resourceRequirements }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified license resource.

```sql
DELETE FROM google.compute.licenses
WHERE license = '{{ license }}'
AND project = '{{ project }}';
```
