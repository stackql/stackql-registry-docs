---
title: liens
hide_title: false
hide_table_of_contents: false
keywords:
  - liens
  - cloudresourcemanager
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

Creates, updates, deletes or gets an <code>lien</code> resource or lists <code>liens</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>liens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudresourcemanager.liens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A system-generated unique identifier for this Lien. Example: `liens/1234abcd` |
| <CopyableCode code="createTime" /> | `string` | The creation time of this Lien. |
| <CopyableCode code="origin" /> | `string` | A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically. Maximum length of 200 characters. Example: 'compute.googleapis.com' |
| <CopyableCode code="parent" /> | `string` | A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens are supported. Example: `projects/1234` |
| <CopyableCode code="reason" /> | `string` | Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200 characters. Example: 'Holds production API key' |
| <CopyableCode code="restrictions" /> | `array` | The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM permission. The server will validate the permissions against those for which Liens are supported. An empty list is meaningless and will be rejected. Example: ['resourcemanager.projects.delete'] |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="liensId" /> | Retrieve a Lien by `name`. Callers of this method will require permission on the `parent` resource. For example, a Lien with a `parent` of `projects/1234` requires permission `resourcemanager.projects.get` |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | List all Liens applied to the `parent` resource. Callers of this method will require permission on the `parent` resource. For example, a Lien with a `parent` of `projects/1234` requires permission `resourcemanager.projects.get`. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Create a Lien which applies to the resource denoted by the `parent` field. Callers of this method will require permission on the `parent` resource. For example, applying to `projects/1234` requires permission `resourcemanager.projects.updateLiens`. NOTE: Some resources may limit the number of Liens which may be applied. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="liensId" /> | Delete a Lien by `name`. Callers of this method will require permission on the `parent` resource. For example, a Lien with a `parent` of `projects/1234` requires permission `resourcemanager.projects.updateLiens`. |

## `SELECT` examples

List all Liens applied to the `parent` resource. Callers of this method will require permission on the `parent` resource. For example, a Lien with a `parent` of `projects/1234` requires permission `resourcemanager.projects.get`.

```sql
SELECT
name,
createTime,
origin,
parent,
reason,
restrictions
FROM google.cloudresourcemanager.liens
WHERE  = '{{  }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>liens</code> resource.

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
INSERT INTO google.cloudresourcemanager.liens (
,
name,
parent,
restrictions,
reason,
origin,
createTime
)
SELECT 
'{{  }}',
'{{ name }}',
'{{ parent }}',
'{{ restrictions }}',
'{{ reason }}',
'{{ origin }}',
'{{ createTime }}'
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
      - name: parent
        value: '{{ parent }}'
      - name: restrictions
        value: '{{ restrictions }}'
      - name: reason
        value: '{{ reason }}'
      - name: origin
        value: '{{ origin }}'
      - name: createTime
        value: '{{ createTime }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified lien resource.

```sql
DELETE FROM google.cloudresourcemanager.liens
WHERE liensId = '{{ liensId }}';
```
