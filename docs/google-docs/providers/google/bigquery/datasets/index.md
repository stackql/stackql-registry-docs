---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - bigquery
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

Creates, updates, deletes, gets or lists a <code>datasets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquery.datasets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. The fully-qualified unique name of the dataset in the format projectId:datasetId. The dataset name without the project name is given in the datasetId field. When creating a new dataset, leave this field blank, and instead specify the datasetId field. |
| <CopyableCode code="description" /> | `string` | Optional. A user-friendly description of the dataset. |
| <CopyableCode code="access" /> | `array` | Optional. An array of objects that define dataset access for one or more entities. You can set this property when inserting or updating a dataset in order to control who is allowed to access the data. If unspecified at dataset creation time, BigQuery adds default dataset access for the following entities: access.specialGroup: projectReaders; access.role: READER; access.specialGroup: projectWriters; access.role: WRITER; access.specialGroup: projectOwners; access.role: OWNER; access.userByEmail: [dataset creator email]; access.role: OWNER; If you patch a dataset, then this field is overwritten by the patched dataset's access field. To add entities, you must supply the entire existing access array in addition to any new entities that you want to add. |
| <CopyableCode code="creationTime" /> | `string` | Output only. The time when this dataset was created, in milliseconds since the epoch. |
| <CopyableCode code="datasetReference" /> | `object` | Identifier for a dataset. |
| <CopyableCode code="defaultCollation" /> | `string` | Optional. Defines the default collation specification of future tables created in the dataset. If a table is created in this dataset without table-level default collation, then the table inherits the dataset default collation, which is applied to the string fields that do not have explicit collation specified. A change to this field affects only tables created afterwards, and does not alter the existing tables. The following values are supported: * 'und:ci': undetermined locale, case insensitive. * '': empty string. Default to case-sensitive behavior. |
| <CopyableCode code="defaultEncryptionConfiguration" /> | `object` | Configuration for Cloud KMS encryption settings. |
| <CopyableCode code="defaultPartitionExpirationMs" /> | `string` | This default partition expiration, expressed in milliseconds. When new time-partitioned tables are created in a dataset where this property is set, the table will inherit this value, propagated as the `TimePartitioning.expirationMs` property on the new table. If you set `TimePartitioning.expirationMs` explicitly when creating a table, the `defaultPartitionExpirationMs` of the containing dataset is ignored. When creating a partitioned table, if `defaultPartitionExpirationMs` is set, the `defaultTableExpirationMs` value is ignored and the table will not be inherit a table expiration deadline. |
| <CopyableCode code="defaultRoundingMode" /> | `string` | Optional. Defines the default rounding mode specification of new tables created within this dataset. During table creation, if this field is specified, the table within this dataset will inherit the default rounding mode of the dataset. Setting the default rounding mode on a table overrides this option. Existing tables in the dataset are unaffected. If columns are defined during that table creation, they will immediately inherit the table's default rounding mode, unless otherwise specified. |
| <CopyableCode code="defaultTableExpirationMs" /> | `string` | Optional. The default lifetime of all tables in the dataset, in milliseconds. The minimum lifetime value is 3600000 milliseconds (one hour). To clear an existing default expiration with a PATCH request, set to 0. Once this property is set, all newly-created tables in the dataset will have an expirationTime property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the expirationTime for a given table is reached, that table will be deleted automatically. If a table's expirationTime is modified or removed before the table expires, or if you provide an explicit expirationTime when creating a table, that value takes precedence over the default expiration time indicated by this property. |
| <CopyableCode code="etag" /> | `string` | Output only. A hash of the resource. |
| <CopyableCode code="externalCatalogDatasetOptions" /> | `object` | Options defining open source compatible datasets living in the BigQuery catalog. Contains metadata of open source database, schema or namespace represented by the current dataset. |
| <CopyableCode code="externalDatasetReference" /> | `object` | Configures the access a dataset defined in an external metadata storage. |
| <CopyableCode code="friendlyName" /> | `string` | Optional. A descriptive name for the dataset. |
| <CopyableCode code="isCaseInsensitive" /> | `boolean` | Optional. TRUE if the dataset and its table names are case-insensitive, otherwise FALSE. By default, this is FALSE, which means the dataset and its table names are case-sensitive. This field does not affect routine references. |
| <CopyableCode code="kind" /> | `string` | Output only. The resource type. |
| <CopyableCode code="labels" /> | `object` | The labels associated with this dataset. You can use these to organize and group your datasets. You can set this property when inserting or updating a dataset. See [Creating and Updating Dataset Labels](https://cloud.google.com/bigquery/docs/creating-managing-labels#creating_and_updating_dataset_labels) for more information. |
| <CopyableCode code="lastModifiedTime" /> | `string` | Output only. The date when this dataset was last modified, in milliseconds since the epoch. |
| <CopyableCode code="linkedDatasetMetadata" /> | `object` | Metadata about the Linked Dataset. |
| <CopyableCode code="linkedDatasetSource" /> | `object` | A dataset source type which refers to another BigQuery dataset. |
| <CopyableCode code="location" /> | `string` | The geographic location where the dataset should reside. See https://cloud.google.com/bigquery/docs/locations for supported locations. |
| <CopyableCode code="maxTimeTravelHours" /> | `string` | Optional. Defines the time travel window in hours. The value can be from 48 to 168 hours (2 to 7 days). The default value is 168 hours if this is not set. |
| <CopyableCode code="resourceTags" /> | `object` | Optional. The [tags](/bigquery/docs/tags) attached to this dataset. Tag keys are globally unique. Tag key is expected to be in the namespaced format, for example "123456789012/environment" where 123456789012 is the ID of the parent organization or project resource for this tag key. Tag value is expected to be the short name, for example "Production". See [Tag definitions](/iam/docs/tags-access-control#definitions) for more details. |
| <CopyableCode code="restrictions" /> | `object` |  |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="selfLink" /> | `string` | Output only. A URL that can be used to access the resource again. You can use this URL in Get or Update requests to the resource. |
| <CopyableCode code="storageBillingModel" /> | `string` | Optional. Updates storage_billing_model for the dataset. |
| <CopyableCode code="tags" /> | `array` | Output only. Tags for the dataset. To provide tags as inputs, use the `resourceTags` field. |
| <CopyableCode code="type" /> | `string` | Output only. Same as `type` in `ListFormatDataset`. The type of the dataset, one of: * DEFAULT - only accessible by owner and authorized accounts, * PUBLIC - accessible by everyone, * LINKED - linked dataset, * EXTERNAL - dataset with definition in external metadata catalog. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="+datasetId, projectId" /> | Returns the dataset specified by datasetID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectId" /> | Lists all datasets in the specified project to which the user has been granted the READER dataset role. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="projectId" /> | Creates a new empty dataset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="+datasetId, projectId" /> | Deletes the dataset specified by the datasetId value. Before you can delete a dataset, you must delete all its tables, either manually or by specifying deleteContents. Immediately after deletion, you can create another dataset with the same name. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="+datasetId, projectId" /> | Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource. This method supports RFC5789 patch semantics. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="+datasetId, projectId" /> | Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="+datasetId, projectId" /> | Undeletes a dataset which is within time travel window based on datasetId. If a time is specified, the dataset version deleted at that time is undeleted, else the last live version is undeleted. |

## `SELECT` examples

Lists all datasets in the specified project to which the user has been granted the READER dataset role.

```sql
SELECT
id,
description,
access,
creationTime,
datasetReference,
defaultCollation,
defaultEncryptionConfiguration,
defaultPartitionExpirationMs,
defaultRoundingMode,
defaultTableExpirationMs,
etag,
externalCatalogDatasetOptions,
externalDatasetReference,
friendlyName,
isCaseInsensitive,
kind,
labels,
lastModifiedTime,
linkedDatasetMetadata,
linkedDatasetSource,
location,
maxTimeTravelHours,
resourceTags,
restrictions,
satisfiesPzi,
satisfiesPzs,
selfLink,
storageBillingModel,
tags,
type
FROM google.bigquery.datasets
WHERE projectId = '{{ projectId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>datasets</code> resource.

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
INSERT INTO google.bigquery.datasets (
projectId,
access,
creationTime,
datasetReference,
defaultCollation,
defaultEncryptionConfiguration,
defaultPartitionExpirationMs,
defaultRoundingMode,
defaultTableExpirationMs,
description,
etag,
externalCatalogDatasetOptions,
externalDatasetReference,
friendlyName,
id,
isCaseInsensitive,
kind,
labels,
lastModifiedTime,
linkedDatasetMetadata,
linkedDatasetSource,
location,
maxTimeTravelHours,
resourceTags,
restrictions,
satisfiesPzi,
satisfiesPzs,
selfLink,
storageBillingModel,
tags,
type
)
SELECT 
'{{ projectId }}',
'{{ access }}',
'{{ creationTime }}',
'{{ datasetReference }}',
'{{ defaultCollation }}',
'{{ defaultEncryptionConfiguration }}',
'{{ defaultPartitionExpirationMs }}',
'{{ defaultRoundingMode }}',
'{{ defaultTableExpirationMs }}',
'{{ description }}',
'{{ etag }}',
'{{ externalCatalogDatasetOptions }}',
'{{ externalDatasetReference }}',
'{{ friendlyName }}',
'{{ id }}',
true|false,
'{{ kind }}',
'{{ labels }}',
'{{ lastModifiedTime }}',
'{{ linkedDatasetMetadata }}',
'{{ linkedDatasetSource }}',
'{{ location }}',
'{{ maxTimeTravelHours }}',
'{{ resourceTags }}',
'{{ restrictions }}',
true|false,
true|false,
'{{ selfLink }}',
'{{ storageBillingModel }}',
'{{ tags }}',
'{{ type }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: access
      value:
        - - name: dataset
            value: '{{ dataset }}'
          - name: domain
            value: '{{ domain }}'
          - name: groupByEmail
            value: '{{ groupByEmail }}'
          - name: iamMember
            value: '{{ iamMember }}'
          - name: role
            value: '{{ role }}'
          - name: routine
            value: '{{ routine }}'
          - name: specialGroup
            value: '{{ specialGroup }}'
          - name: userByEmail
            value: '{{ userByEmail }}'
          - name: view
            value: '{{ view }}'
    - name: creationTime
      value: '{{ creationTime }}'
    - name: datasetReference
      value: '{{ datasetReference }}'
    - name: defaultCollation
      value: '{{ defaultCollation }}'
    - name: defaultEncryptionConfiguration
      value: '{{ defaultEncryptionConfiguration }}'
    - name: defaultPartitionExpirationMs
      value: '{{ defaultPartitionExpirationMs }}'
    - name: defaultRoundingMode
      value: '{{ defaultRoundingMode }}'
    - name: defaultTableExpirationMs
      value: '{{ defaultTableExpirationMs }}'
    - name: description
      value: '{{ description }}'
    - name: etag
      value: '{{ etag }}'
    - name: externalCatalogDatasetOptions
      value: '{{ externalCatalogDatasetOptions }}'
    - name: externalDatasetReference
      value: '{{ externalDatasetReference }}'
    - name: friendlyName
      value: '{{ friendlyName }}'
    - name: id
      value: '{{ id }}'
    - name: isCaseInsensitive
      value: '{{ isCaseInsensitive }}'
    - name: kind
      value: '{{ kind }}'
    - name: labels
      value: '{{ labels }}'
    - name: lastModifiedTime
      value: '{{ lastModifiedTime }}'
    - name: linkedDatasetMetadata
      value: '{{ linkedDatasetMetadata }}'
    - name: linkedDatasetSource
      value: '{{ linkedDatasetSource }}'
    - name: location
      value: '{{ location }}'
    - name: maxTimeTravelHours
      value: '{{ maxTimeTravelHours }}'
    - name: resourceTags
      value: '{{ resourceTags }}'
    - name: restrictions
      value: '{{ restrictions }}'
    - name: satisfiesPzi
      value: '{{ satisfiesPzi }}'
    - name: satisfiesPzs
      value: '{{ satisfiesPzs }}'
    - name: selfLink
      value: '{{ selfLink }}'
    - name: storageBillingModel
      value: '{{ storageBillingModel }}'
    - name: tags
      value:
        - - name: tagKey
            value: '{{ tagKey }}'
          - name: tagValue
            value: '{{ tagValue }}'
    - name: type
      value: '{{ type }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>datasets</code> resource.

```sql
/*+ update */
UPDATE google.bigquery.datasets
SET 
access = '{{ access }}',
creationTime = '{{ creationTime }}',
datasetReference = '{{ datasetReference }}',
defaultCollation = '{{ defaultCollation }}',
defaultEncryptionConfiguration = '{{ defaultEncryptionConfiguration }}',
defaultPartitionExpirationMs = '{{ defaultPartitionExpirationMs }}',
defaultRoundingMode = '{{ defaultRoundingMode }}',
defaultTableExpirationMs = '{{ defaultTableExpirationMs }}',
description = '{{ description }}',
etag = '{{ etag }}',
externalCatalogDatasetOptions = '{{ externalCatalogDatasetOptions }}',
externalDatasetReference = '{{ externalDatasetReference }}',
friendlyName = '{{ friendlyName }}',
id = '{{ id }}',
isCaseInsensitive = true|false,
kind = '{{ kind }}',
labels = '{{ labels }}',
lastModifiedTime = '{{ lastModifiedTime }}',
linkedDatasetMetadata = '{{ linkedDatasetMetadata }}',
linkedDatasetSource = '{{ linkedDatasetSource }}',
location = '{{ location }}',
maxTimeTravelHours = '{{ maxTimeTravelHours }}',
resourceTags = '{{ resourceTags }}',
restrictions = '{{ restrictions }}',
satisfiesPzi = true|false,
satisfiesPzs = true|false,
selfLink = '{{ selfLink }}',
storageBillingModel = '{{ storageBillingModel }}',
tags = '{{ tags }}',
type = '{{ type }}'
WHERE 
+datasetId = '{{ +datasetId }}'
AND projectId = '{{ projectId }}';
```

## `UPDATE` example

Replaces all fields in the specified <code>datasets</code> resource.

```sql
/*+ update */
REPLACE google.bigquery.datasets
SET 
access = '{{ access }}',
creationTime = '{{ creationTime }}',
datasetReference = '{{ datasetReference }}',
defaultCollation = '{{ defaultCollation }}',
defaultEncryptionConfiguration = '{{ defaultEncryptionConfiguration }}',
defaultPartitionExpirationMs = '{{ defaultPartitionExpirationMs }}',
defaultRoundingMode = '{{ defaultRoundingMode }}',
defaultTableExpirationMs = '{{ defaultTableExpirationMs }}',
description = '{{ description }}',
etag = '{{ etag }}',
externalCatalogDatasetOptions = '{{ externalCatalogDatasetOptions }}',
externalDatasetReference = '{{ externalDatasetReference }}',
friendlyName = '{{ friendlyName }}',
id = '{{ id }}',
isCaseInsensitive = true|false,
kind = '{{ kind }}',
labels = '{{ labels }}',
lastModifiedTime = '{{ lastModifiedTime }}',
linkedDatasetMetadata = '{{ linkedDatasetMetadata }}',
linkedDatasetSource = '{{ linkedDatasetSource }}',
location = '{{ location }}',
maxTimeTravelHours = '{{ maxTimeTravelHours }}',
resourceTags = '{{ resourceTags }}',
restrictions = '{{ restrictions }}',
satisfiesPzi = true|false,
satisfiesPzs = true|false,
selfLink = '{{ selfLink }}',
storageBillingModel = '{{ storageBillingModel }}',
tags = '{{ tags }}',
type = '{{ type }}'
WHERE 
+datasetId = '{{ +datasetId }}'
AND projectId = '{{ projectId }}';
```

## `DELETE` example

Deletes the specified <code>datasets</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigquery.datasets
WHERE +datasetId = '{{ +datasetId }}'
AND projectId = '{{ projectId }}';
```
