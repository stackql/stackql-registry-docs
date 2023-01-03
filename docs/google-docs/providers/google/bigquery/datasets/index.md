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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output-only] The fully-qualified unique name of the dataset in the format projectId:datasetId. The dataset name without the project name is given in the datasetId field. When creating a new dataset, leave this field blank, and instead specify the datasetId field. |
| `description` | `string` | [Optional] A user-friendly description of the dataset. |
| `friendlyName` | `string` | [Optional] A descriptive name for the dataset. |
| `access` | `array` | [Optional] An array of objects that define dataset access for one or more entities. You can set this property when inserting or updating a dataset in order to control who is allowed to access the data. If unspecified at dataset creation time, BigQuery adds default dataset access for the following entities: access.specialGroup: projectReaders; access.role: READER; access.specialGroup: projectWriters; access.role: WRITER; access.specialGroup: projectOwners; access.role: OWNER; access.userByEmail: [dataset creator email]; access.role: OWNER; |
| `selfLink` | `string` | [Output-only] A URL that can be used to access the resource again. You can use this URL in Get or Update requests to the resource. |
| `creationTime` | `string` | [Output-only] The time when this dataset was created, in milliseconds since the epoch. |
| `location` | `string` | The geographic location where the dataset should reside. The default value is US. See details at https://cloud.google.com/bigquery/docs/locations. |
| `defaultTableExpirationMs` | `string` | [Optional] The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour). Once this property is set, all newly-created tables in the dataset will have an expirationTime property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the expirationTime for a given table is reached, that table will be deleted automatically. If a table's expirationTime is modified or removed before the table expires, or if you provide an explicit expirationTime when creating a table, that value takes precedence over the default expiration time indicated by this property. |
| `defaultCollation` | `string` | [Output-only] The default collation of the dataset. |
| `etag` | `string` | [Output-only] A hash of the resource. |
| `defaultEncryptionConfiguration` | `object` |  |
| `maxTimeTravelHours` | `string` | [Optional] Number of hours for the max time travel for all tables in the dataset. |
| `tags` | `array` | [Optional]The tags associated with this dataset. Tag keys are globally unique. |
| `lastModifiedTime` | `string` | [Output-only] The date when this dataset or any of its tables was last modified, in milliseconds since the epoch. |
| `satisfiesPzs` | `boolean` | [Output-only] Reserved for future use. |
| `labels` | `object` | The labels associated with this dataset. You can use these to organize and group your datasets. You can set this property when inserting or updating a dataset. See Creating and Updating Dataset Labels for more information. |
| `defaultPartitionExpirationMs` | `string` | [Optional] The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set, all newly-created partitioned tables in the dataset will have an expirationMs property in the timePartitioning settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of defaultTableExpirationMs for partitioned tables: only one of defaultTableExpirationMs and defaultPartitionExpirationMs will be used for any new partitioned table. If you provide an explicit timePartitioning.expirationMs when creating or updating a partitioned table, that value takes precedence over the default partition expiration time indicated by this property. |
| `datasetReference` | `object` |  |
| `kind` | `string` | [Output-only] The resource type. |
| `isCaseInsensitive` | `boolean` | [Optional] Indicates if table names are case insensitive in the dataset. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datasetId, projectId` | Returns the dataset specified by datasetID. |
| `list` | `SELECT` | `projectId` | Lists all datasets in the specified project to which you have been granted the READER dataset role. |
| `insert` | `INSERT` | `projectId` | Creates a new empty dataset. |
| `delete` | `DELETE` | `datasetId, projectId` | Deletes the dataset specified by the datasetId value. Before you can delete a dataset, you must delete all its tables, either manually or by specifying deleteContents. Immediately after deletion, you can create another dataset with the same name. |
| `patch` | `EXEC` | `datasetId, projectId` | Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource. This method supports patch semantics. |
| `update` | `EXEC` | `datasetId, projectId` | Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource. |
