---
title: sinks
hide_title: false
hide_table_of_contents: false
keywords:
  - sinks
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

Creates, updates, deletes, gets or lists a <code>sinks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.sinks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The client-assigned sink identifier, unique within the project.For example: "my-syslog-errors-to-pubsub".Sink identifiers are limited to 100 characters and can include only the following characters: upper and lower-case alphanumeric characters, underscores, hyphens, periods.First character has to be alphanumeric. |
| <CopyableCode code="description" /> | `string` | Optional. A description of this sink.The maximum length of the description is 8000 characters. |
| <CopyableCode code="bigqueryOptions" /> | `object` | Options that change functionality of a sink exporting data to BigQuery. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of the sink.This field may not be present for older sinks. |
| <CopyableCode code="destination" /> | `string` | Required. The export destination: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" "logging.googleapis.com/projects/[PROJECT_ID]" "logging.googleapis.com/projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]" The sink's writer_identity, set when the sink is created, must have permission to write to the destination or else the log entries are not exported. For more information, see Exporting Logs with Sinks (https://cloud.google.com/logging/docs/api/tasks/exporting-logs). |
| <CopyableCode code="disabled" /> | `boolean` | Optional. If set to true, then this sink is disabled and it does not export any log entries. |
| <CopyableCode code="exclusions" /> | `array` | Optional. Log entries that match any of these exclusion filters will not be exported.If a log entry is matched by both filter and one of exclusion_filters it will not be exported. |
| <CopyableCode code="filter" /> | `string` | Optional. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries). The only exported log entries are those that are in the resource owning the sink and that match the filter.For example:logName="projects/[PROJECT_ID]/logs/[LOG_ID]" AND severity>=ERROR |
| <CopyableCode code="includeChildren" /> | `boolean` | Optional. This field applies only to sinks owned by organizations and folders. If the field is false, the default, only the logs owned by the sink's parent resource are available for export. If the field is true, then log entries from all the projects, folders, and billing accounts contained in the sink's parent resource are also available for export. Whether a particular log entry from the children is exported depends on the sink's filter expression.For example, if this field is true, then the filter resource.type=gce_instance would export all Compute Engine VM instance log entries from all projects in the sink's parent.To only export entries from certain child projects, filter on the project part of the log name:logName:("projects/test-project1/" OR "projects/test-project2/") AND resource.type=gce_instance |
| <CopyableCode code="interceptChildren" /> | `boolean` | Optional. This field applies only to sinks owned by organizations and folders.When the value of 'intercept_children' is true, the following restrictions apply: The sink must have the include_children flag set to true. The sink destination must be a Cloud project.Also, the following behaviors apply: Any logs matched by the sink won't be included by non-_Required sinks owned by child resources. The sink appears in the results of a ListSinks call from a child resource if the value of the filter field in its request is either 'in_scope("ALL")' or 'in_scope("ANCESTOR")'. |
| <CopyableCode code="outputVersionFormat" /> | `string` | Deprecated. This field is unused. |
| <CopyableCode code="resourceName" /> | `string` | Output only. The resource name of the sink. "projects/[PROJECT_ID]/sinks/[SINK_NAME] "organizations/[ORGANIZATION_ID]/sinks/[SINK_NAME] "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_NAME] "folders/[FOLDER_ID]/sinks/[SINK_NAME] For example: projects/my_project/sinks/SINK_NAME |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of the sink.This field may not be present for older sinks. |
| <CopyableCode code="writerIdentity" /> | `string` | Output only. An IAM identity—a service account or group—under which Cloud Logging writes the exported log entries to the sink's destination. This field is either set by specifying custom_writer_identity or set automatically by sinks.create and sinks.update based on the value of unique_writer_identity in those methods.Until you grant this identity write-access to the destination, log entry exports from this sink will fail. For more information, see Granting Access for a Resource (https://cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource). Consult the destination service's documentation to determine the appropriate IAM roles to assign to the identity.Sinks that have a destination that is a log bucket in the same project as the sink cannot have a writer_identity and no additional permissions are required. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_sinks_get" /> | `SELECT` | <CopyableCode code="billingAccountsId, sinksId" /> | Gets a sink. |
| <CopyableCode code="billing_accounts_sinks_list" /> | `SELECT` | <CopyableCode code="billingAccountsId" /> | Lists sinks. |
| <CopyableCode code="folders_sinks_get" /> | `SELECT` | <CopyableCode code="foldersId, sinksId" /> | Gets a sink. |
| <CopyableCode code="folders_sinks_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists sinks. |
| <CopyableCode code="organizations_sinks_get" /> | `SELECT` | <CopyableCode code="organizationsId, sinksId" /> | Gets a sink. |
| <CopyableCode code="organizations_sinks_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists sinks. |
| <CopyableCode code="projects_sinks_get" /> | `SELECT` | <CopyableCode code="projectsId, sinksId" /> | Gets a sink. |
| <CopyableCode code="projects_sinks_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists sinks. |
| <CopyableCode code="sinks_get" /> | `SELECT` | <CopyableCode code="sinkName" /> | Gets a sink. |
| <CopyableCode code="sinks_list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Lists sinks. |
| <CopyableCode code="billing_accounts_sinks_create" /> | `INSERT` | <CopyableCode code="billingAccountsId" /> | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| <CopyableCode code="folders_sinks_create" /> | `INSERT` | <CopyableCode code="foldersId" /> | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| <CopyableCode code="organizations_sinks_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| <CopyableCode code="projects_sinks_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| <CopyableCode code="sinks_create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| <CopyableCode code="billing_accounts_sinks_delete" /> | `DELETE` | <CopyableCode code="billingAccountsId, sinksId" /> | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| <CopyableCode code="folders_sinks_delete" /> | `DELETE` | <CopyableCode code="foldersId, sinksId" /> | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| <CopyableCode code="organizations_sinks_delete" /> | `DELETE` | <CopyableCode code="organizationsId, sinksId" /> | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| <CopyableCode code="projects_sinks_delete" /> | `DELETE` | <CopyableCode code="projectsId, sinksId" /> | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| <CopyableCode code="sinks_delete" /> | `DELETE` | <CopyableCode code="sinkName" /> | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| <CopyableCode code="billing_accounts_sinks_patch" /> | `UPDATE` | <CopyableCode code="billingAccountsId, sinksId" /> | Updates a sink. This method replaces the values of the destination and filter fields of the existing sink with the corresponding values from the new sink.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| <CopyableCode code="folders_sinks_patch" /> | `UPDATE` | <CopyableCode code="foldersId, sinksId" /> | Updates a sink. This method replaces the values of the destination and filter fields of the existing sink with the corresponding values from the new sink.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| <CopyableCode code="organizations_sinks_patch" /> | `UPDATE` | <CopyableCode code="organizationsId, sinksId" /> | Updates a sink. This method replaces the values of the destination and filter fields of the existing sink with the corresponding values from the new sink.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| <CopyableCode code="projects_sinks_patch" /> | `UPDATE` | <CopyableCode code="projectsId, sinksId" /> | Updates a sink. This method replaces the values of the destination and filter fields of the existing sink with the corresponding values from the new sink.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| <CopyableCode code="billing_accounts_sinks_update" /> | `REPLACE` | <CopyableCode code="billingAccountsId, sinksId" /> | Updates a sink. This method replaces the values of the destination and filter fields of the existing sink with the corresponding values from the new sink.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| <CopyableCode code="folders_sinks_update" /> | `REPLACE` | <CopyableCode code="foldersId, sinksId" /> | Updates a sink. This method replaces the values of the destination and filter fields of the existing sink with the corresponding values from the new sink.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| <CopyableCode code="organizations_sinks_update" /> | `REPLACE` | <CopyableCode code="organizationsId, sinksId" /> | Updates a sink. This method replaces the values of the destination and filter fields of the existing sink with the corresponding values from the new sink.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| <CopyableCode code="projects_sinks_update" /> | `REPLACE` | <CopyableCode code="projectsId, sinksId" /> | Updates a sink. This method replaces the values of the destination and filter fields of the existing sink with the corresponding values from the new sink.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| <CopyableCode code="sinks_update" /> | `REPLACE` | <CopyableCode code="sinkName" /> | Updates a sink. This method replaces the values of the destination and filter fields of the existing sink with the corresponding values from the new sink.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |

## `SELECT` examples

Gets a sink.

```sql
SELECT
name,
description,
bigqueryOptions,
createTime,
destination,
disabled,
exclusions,
filter,
includeChildren,
interceptChildren,
outputVersionFormat,
resourceName,
updateTime,
writerIdentity
FROM google.logging.sinks
WHERE sinkName = '{{ sinkName }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sinks</code> resource.

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
INSERT INTO google.logging.sinks (
foldersId,
destination,
filter,
description,
disabled,
exclusions,
outputVersionFormat,
includeChildren,
interceptChildren,
bigqueryOptions
)
SELECT 
'{{ foldersId }}',
'{{ destination }}',
'{{ filter }}',
'{{ description }}',
{{ disabled }},
'{{ exclusions }}',
'{{ outputVersionFormat }}',
{{ includeChildren }},
{{ interceptChildren }},
'{{ bigqueryOptions }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: resourceName
      value: string
    - name: destination
      value: string
    - name: filter
      value: string
    - name: description
      value: string
    - name: disabled
      value: boolean
    - name: exclusions
      value:
        - - name: name
            value: string
          - name: description
            value: string
          - name: filter
            value: string
          - name: disabled
            value: boolean
          - name: createTime
            value: string
          - name: updateTime
            value: string
    - name: outputVersionFormat
      value: string
    - name: writerIdentity
      value: string
    - name: includeChildren
      value: boolean
    - name: interceptChildren
      value: boolean
    - name: bigqueryOptions
      value:
        - name: usePartitionedTables
          value: boolean
        - name: usesTimestampColumnPartitioning
          value: boolean
    - name: createTime
      value: string
    - name: updateTime
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sinks</code> resource.

```sql
/*+ update */
UPDATE google.logging.sinks
SET 
destination = '{{ destination }}',
filter = '{{ filter }}',
description = '{{ description }}',
disabled = true|false,
exclusions = '{{ exclusions }}',
outputVersionFormat = '{{ outputVersionFormat }}',
includeChildren = true|false,
interceptChildren = true|false,
bigqueryOptions = '{{ bigqueryOptions }}'
WHERE 
foldersId = '{{ foldersId }}'
AND sinksId = '{{ sinksId }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>sinks</code> resource.

```sql
/*+ update */
REPLACE google.logging.sinks
SET 
destination = '{{ destination }}',
filter = '{{ filter }}',
description = '{{ description }}',
disabled = true|false,
exclusions = '{{ exclusions }}',
outputVersionFormat = '{{ outputVersionFormat }}',
includeChildren = true|false,
interceptChildren = true|false,
bigqueryOptions = '{{ bigqueryOptions }}'
WHERE 
sinkName = '{{ sinkName }}';
```

## `DELETE` example

Deletes the specified <code>sinks</code> resource.

```sql
/*+ delete */
DELETE FROM google.logging.sinks
WHERE sinkName = '{{ sinkName }}';
```
