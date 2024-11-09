---
title: consumer_shared_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_shared_resources
  - stream_sharing
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>consumer_shared_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_shared_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.stream_sharing.consumer_shared_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | Description of consumer resource |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="cloud" /> | `string` | The cloud service provider of the provider shared cluster. |
| <CopyableCode code="display_name" /> | `string` | Consumer resource display name |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="logo_url" /> | `string` | Resource logo url |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="network_connection_types" /> | `array` | The network connection types of the provider shared cluster. If the shared cluster is on public internet,
then the list will be empty |
| <CopyableCode code="organization_contact" /> | `string` | Email of the shared resource's organization contact |
| <CopyableCode code="organization_description" /> | `string` | Shared resource's organization description |
| <CopyableCode code="organization_name" /> | `string` | Shared resource's organization name |
| <CopyableCode code="schemas" /> | `array` | List of schemas in JSON format. This field is work in progress and subject to changes. |
| <CopyableCode code="tags" /> | `array` | list of tags |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cdx_v1consumer_shared_resource" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to read a consumer shared resource. |
| <CopyableCode code="list_cdx_v1consumer_shared_resources" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all consumer shared resources. |
| <CopyableCode code="image_cdx_v1consumer_shared_resource" /> | `EXEC` | <CopyableCode code="file_name, id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Returns the image file for the shared resource |
| <CopyableCode code="network_cdx_v1consumer_shared_resource" /> | `EXEC` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Returns network information of the shared resource |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all consumer shared resources.


```sql
SELECT
id,
description,
api_version,
cloud,
display_name,
kind,
logo_url,
metadata,
network_connection_types,
organization_contact,
organization_description,
organization_name,
schemas,
tags
FROM confluent.stream_sharing.consumer_shared_resources
;
```