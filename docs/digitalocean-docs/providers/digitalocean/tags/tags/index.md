---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - tags
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.tags.tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the tag. Tags may contain letters, numbers, colons, dashes, and underscores. There is a limit of 255 characters per tag. **Note:** Tag names are case stable, which means the capitalization you use when you first create a tag is canonical. When working with tags in the API, you must use the tag's canonical capitalization. For example, if you create a tag named "PROD", the URL to add that tag to a resource would be `https://api.digitalocean.com/v2/tags/PROD/resources` (not `/v2/tags/prod/resources`). Tagged resources in the control panel will always display the canonical capitalization. For example, if you create a tag named "PROD", you can tag resources in the control panel by entering "prod". The tag will still display with its canonical capitalization, "PROD". |
| <CopyableCode code="resources" /> | `object` | Tagged Resource Statistics include metadata regarding the resource type that has been tagged. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="tags_get" /> | `SELECT` | <CopyableCode code="tag_id" /> | To retrieve an individual tag, you can send a `GET` request to `/v2/tags/$TAG_NAME`. |
| <CopyableCode code="tags_list" /> | `SELECT` | <CopyableCode code="" /> | To list all of your tags, you can send a GET request to `/v2/tags`. |
| <CopyableCode code="tags_create" /> | `INSERT` | <CopyableCode code="" /> | To create a tag you can send a POST request to `/v2/tags` with a `name` attribute. |
| <CopyableCode code="tags_delete" /> | `DELETE` | <CopyableCode code="tag_id" /> | A tag can be deleted by sending a `DELETE` request to `/v2/tags/$TAG_NAME`. Deleting a tag also untags all the resources that have previously been tagged by the Tag |

## `SELECT` examples

To list all of your tags, you can send a GET request to `/v2/tags`.


```sql
SELECT
name,
resources
FROM digitalocean.tags.tags
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tags</code> resource.

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
INSERT INTO digitalocean.tags.tags (
data__name,
data__resources
)
SELECT 
'{{ name }}',
'{{ resources }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: tags
  props:
    - name: name
      value: string
    - name: resources
      props:
        - name: count
          value: integer
        - name: last_tagged_uri
          value: string
        - name: droplets
          props:
            - name: count
              value: integer
            - name: last_tagged_uri
              value: string
        - name: imgages
          props:
            - name: count
              value: integer
            - name: last_tagged_uri
              value: string
        - name: volumes
          props:
            - name: count
              value: integer
            - name: last_tagged_uri
              value: string
        - name: volume_snapshots
          props:
            - name: count
              value: integer
            - name: last_tagged_uri
              value: string
        - name: databases
          props:
            - name: count
              value: integer
            - name: last_tagged_uri
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>tags</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.tags.tags
WHERE tag_id = '{{ tag_id }}';
```
