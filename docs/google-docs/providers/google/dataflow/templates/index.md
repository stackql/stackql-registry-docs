
---
title: templates
hide_title: false
hide_table_of_contents: false
keywords:
  - templates
  - dataflow
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

Creates, updates, deletes or gets an <code>template</code> resource or lists <code>templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataflow.templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="metadata" /> | `object` | Metadata describing a template. |
| <CopyableCode code="runtimeMetadata" /> | `object` | RuntimeMetadata describing a runtime environment. |
| <CopyableCode code="status" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="templateType" /> | `string` | Template Type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_templates_get" /> | `SELECT` | <CopyableCode code="location, projectId" /> | Get the template associated with a template. To get the template, we recommend using `projects.locations.templates.get` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.templates.get` is not recommended, because only templates that are running in `us-central1` are retrieved. |
| <CopyableCode code="projects_templates_get" /> | `SELECT` | <CopyableCode code="projectId" /> | Get the template associated with a template. To get the template, we recommend using `projects.locations.templates.get` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.templates.get` is not recommended, because only templates that are running in `us-central1` are retrieved. |
| <CopyableCode code="projects_locations_templates_create" /> | `INSERT` | <CopyableCode code="location, projectId" /> | Creates a Cloud Dataflow job from a template. Do not enter confidential information when you supply string values using the API. To create a job, we recommend using `projects.locations.templates.create` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.templates.create` is not recommended, because your job will always start in `us-central1`. |
| <CopyableCode code="projects_templates_create" /> | `INSERT` | <CopyableCode code="projectId" /> | Creates a Cloud Dataflow job from a template. Do not enter confidential information when you supply string values using the API. To create a job, we recommend using `projects.locations.templates.create` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.templates.create` is not recommended, because your job will always start in `us-central1`. |
| <CopyableCode code="projects_locations_templates_launch" /> | `EXEC` | <CopyableCode code="location, projectId" /> | Launches a template. To launch a template, we recommend using `projects.locations.templates.launch` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.templates.launch` is not recommended, because jobs launched from the template will always start in `us-central1`. |
| <CopyableCode code="projects_templates_launch" /> | `EXEC` | <CopyableCode code="projectId" /> | Launches a template. To launch a template, we recommend using `projects.locations.templates.launch` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.templates.launch` is not recommended, because jobs launched from the template will always start in `us-central1`. |

## `SELECT` examples

Get the template associated with a template. To get the template, we recommend using `projects.locations.templates.get` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.templates.get` is not recommended, because only templates that are running in `us-central1` are retrieved.

```sql
SELECT
metadata,
runtimeMetadata,
status,
templateType
FROM google.dataflow.templates
WHERE projectId = '{{ projectId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>templates</code> resource.

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
INSERT INTO google.dataflow.templates (
projectId,
jobName,
gcsPath,
parameters,
environment,
location
)
SELECT 
'{{ projectId }}',
'{{ jobName }}',
'{{ gcsPath }}',
'{{ parameters }}',
'{{ environment }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: jobName
        value: '{{ jobName }}'
      - name: gcsPath
        value: '{{ gcsPath }}'
      - name: parameters
        value: '{{ parameters }}'
      - name: environment
        value: '{{ environment }}'
      - name: location
        value: '{{ location }}'

```
</TabItem>
</Tabs>
