---
title: custom_connector_plugins
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_connector_plugins
  - connect
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




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
| <CopyableCode code="connector_type" /> | `string` | Custom Connector type.<br /> |
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
| <CopyableCode code="get_connect_v1custom_connector_plugin" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to read a custom connector plugin. |
| <CopyableCode code="list_connect_v1custom_connector_plugins" /> | `SELECT` |  | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve a sorted, filtered, paginated list of all custom connector plugins.<br /><br />If no `cloud` filter is specified, returns custom connector plugins from all clouds.<br /> |
| <CopyableCode code="create_connect_v1custom_connector_plugin" /> | `INSERT` |  | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to create a custom connector plugin. |
| <CopyableCode code="delete_connect_v1custom_connector_plugin" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to delete a custom connector plugin. |
| <CopyableCode code="update_connect_v1custom_connector_plugin" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to update a custom connector plugin.<br /><br /> |
