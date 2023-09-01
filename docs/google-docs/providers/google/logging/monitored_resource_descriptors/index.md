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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitored_resource_descriptors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.monitored_resource_descriptors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Optional. The resource name of the monitored resource descriptor: "projects/&#123;project_id&#125;/monitoredResourceDescriptors/&#123;type&#125;" where &#123;type&#125; is the value of the type field in this object and &#123;project_id&#125; is a project ID that provides API-specific context for accessing the type. APIs that do not use project information can use the resource name format "monitoredResourceDescriptors/&#123;type&#125;". |
| `description` | `string` | Optional. A detailed description of the monitored resource type that might be used in documentation. |
| `launchStage` | `string` | Optional. The launch stage of the monitored resource definition. |
| `type` | `string` | Required. The monitored resource type. For example, the type "cloudsql_database" represents databases in Google Cloud SQL. For a list of types, see Monitoring resource types (https://cloud.google.com/monitoring/api/resources) and Logging resource types (https://cloud.google.com/logging/docs/api/v2/resource-list). |
| `displayName` | `string` | Optional. A concise name for the monitored resource type that might be displayed in user interfaces. It should be a Title Cased Noun Phrase, without any article or other determiners. For example, "Google Cloud SQL Database". |
| `labels` | `array` | Required. A set of labels used to describe instances of this monitored resource type. For example, an individual Google Cloud SQL database is identified by values for the labels "database_id" and "zone". |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `monitored_resource_descriptors_list` | `SELECT` |  |
| `_monitored_resource_descriptors_list` | `EXEC` |  |
