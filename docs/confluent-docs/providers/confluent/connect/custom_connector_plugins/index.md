---
title: custom_connector_plugins
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_connector_plugins
  - connect
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>custom_connector_plugins</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_connector_plugins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.connect.custom_connector_plugins" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | Description of Custom Connector Plugin. |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="cloud" /> | `string` | Cloud provider where the Custom Connector Plugin archive is uploaded. |
| <CopyableCode code="connector_class" /> | `string` | Java class or alias for connector. You can get connector class from connector documentation provided by developer. |
| <CopyableCode code="connector_type" /> | `string` | Custom Connector type. |
| <CopyableCode code="content_format" /> | `string` | Archive format of Custom Connector Plugin. |
| <CopyableCode code="display_name" /> | `string` | Display name of Custom Connector Plugin. |
| <CopyableCode code="documentation_link" /> | `string` | Document link of Custom Connector Plugin. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="sensitive_config_properties" /> | `array` | A sensitive property is a connector configuration property that must be hidden after a user enters property value when setting up connector. |
| <CopyableCode code="upload_source" /> | `object` | [immutable] Upload source of Custom Connector Plugin. Only required in `create` request, will be ignored in `read`, `update` or `list`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_connect_v1custom_connector_plugin" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read a custom connector plugin. |
| <CopyableCode code="list_connect_v1custom_connector_plugins" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all custom connector plugins. If no `cloud` filter is specified, returns custom connector plugins from all clouds. |
| <CopyableCode code="create_connect_v1custom_connector_plugin" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to create a custom connector plugin. |
| <CopyableCode code="delete_connect_v1custom_connector_plugin" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete a custom connector plugin. |
| <CopyableCode code="update_connect_v1custom_connector_plugin" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to update a custom connector plugin. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all custom connector plugins. If no `cloud` filter is specified, returns custom connector plugins from all clouds.


```sql
SELECT
id,
description,
api_version,
cloud,
connector_class,
connector_type,
content_format,
display_name,
documentation_link,
kind,
metadata,
sensitive_config_properties,
upload_source
FROM confluent.connect.custom_connector_plugins
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_connector_plugins</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO confluent.connect.custom_connector_plugins (
data__display_name,
data__description,
data__documentation_link,
data__connector_class,
data__connector_type,
data__cloud,
data__sensitive_config_properties,
data__upload_source
)
SELECT 
'{{ display_name }}',
'{{ description }}',
'{{ documentation_link }}',
'{{ connector_class }}',
'{{ connector_type }}',
'{{ cloud }}',
'{{ sensitive_config_properties }}',
'{{ upload_source }}'
;
```
</TabItem>

    <TabItem value="required">

    ```sql
    /*+ create */
    INSERT INTO confluent.connect.custom_connector_plugins (
    data__display_name,
data__connector_class,
data__connector_type,
data__upload_source
    )
    SELECT 
    '{{ display_name }}',
'{{ connector_class }}',
'{{ connector_type }}',
'{{ upload_source }}'
    ;
    ```
    </TabItem>
    
<TabItem value="manifest">

```yaml
- name: custom_connector_plugins
  props:
    - name: display_name
      value: string
    - name: description
      value: string
    - name: documentation_link
      value: string
    - name: connector_class
      value: string
    - name: connector_type
      value: string
    - name: cloud
      value: string
    - name: sensitive_config_properties
      value: array
    - name: upload_source
      props:
        - name: location
          value: string
        - name: upload_id
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>custom_connector_plugins</code> resource.

```sql
/*+ update */
UPDATE confluent.connect.custom_connector_plugins
SET 
display_name = '{{ display_name }}',
description = '{{ description }}',
documentation_link = '{{ documentation_link }}',
sensitive_config_properties = '{{ sensitive_config_properties }}',
upload_source = '{{ upload_source }}'
WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>custom_connector_plugins</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.connect.custom_connector_plugins
WHERE id = '{{ id }}';
```
