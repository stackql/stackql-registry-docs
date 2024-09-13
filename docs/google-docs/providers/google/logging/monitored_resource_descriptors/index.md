---
title: monitored_resource_descriptors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitored_resource_descriptors
  - logging
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

Creates, updates, deletes or gets an <code>monitored_resource_descriptor</code> resource or lists <code>monitored_resource_descriptors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitored_resource_descriptors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.monitored_resource_descriptors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optional. The resource name of the monitored resource descriptor: "projects/{project_id}/monitoredResourceDescriptors/{type}" where {type} is the value of the type field in this object and {project_id} is a project ID that provides API-specific context for accessing the type. APIs that do not use project information can use the resource name format "monitoredResourceDescriptors/{type}". |
| <CopyableCode code="description" /> | `string` | Optional. A detailed description of the monitored resource type that might be used in documentation. |
| <CopyableCode code="displayName" /> | `string` | Optional. A concise name for the monitored resource type that might be displayed in user interfaces. It should be a Title Cased Noun Phrase, without any article or other determiners. For example, "Google Cloud SQL Database". |
| <CopyableCode code="labels" /> | `array` | Required. A set of labels used to describe instances of this monitored resource type. For example, an individual Google Cloud SQL database is identified by values for the labels "database_id" and "zone". |
| <CopyableCode code="launchStage" /> | `string` | Optional. The launch stage of the monitored resource definition. |
| <CopyableCode code="type" /> | `string` | Required. The monitored resource type. For example, the type "cloudsql_database" represents databases in Google Cloud SQL. For a list of types, see Monitored resource types (https://cloud.google.com/monitoring/api/resources) and Logging resource types (https://cloud.google.com/logging/docs/api/v2/resource-list). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitored_resource_descriptors_list" /> | `SELECT` | <CopyableCode code="" /> | Lists the descriptors for monitored resource types used by Logging. |

## `SELECT` examples

Lists the descriptors for monitored resource types used by Logging.

```sql
SELECT
name,
description,
displayName,
labels,
launchStage,
type
FROM google.logging.monitored_resource_descriptors
WHERE  = '{{  }}'; 
```
