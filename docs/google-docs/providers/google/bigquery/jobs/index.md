---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquery.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. Opaque ID field of the job. |
| <CopyableCode code="configuration" /> | `object` |  |
| <CopyableCode code="etag" /> | `string` | Output only. A hash of this resource. |
| <CopyableCode code="jobCreationReason" /> | `object` | Reason about why a Job was created from a [`jobs.query`](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query) method when used with `JOB_CREATION_OPTIONAL` Job creation mode. For [`jobs.insert`](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert) method calls it will always be `REQUESTED`. This feature is not yet available. Jobs will always be created. |
| <CopyableCode code="jobReference" /> | `object` | A job reference is a fully qualified identifier for referring to a job. |
| <CopyableCode code="kind" /> | `string` | Output only. The type of the resource. |
| <CopyableCode code="principal_subject" /> | `string` | Output only. [Full-projection-only] String representation of identity of requesting party. Populated for both first- and third-party identities. Only present for APIs that support third-party identities. |
| <CopyableCode code="selfLink" /> | `string` | Output only. A URL that can be used to access the resource again. |
| <CopyableCode code="statistics" /> | `object` | Statistics for a single job execution. |
| <CopyableCode code="status" /> | `object` |  |
| <CopyableCode code="user_email" /> | `string` | Output only. Email address of the user who ran the job. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="+jobId, projectId" /> | Returns information about a specific job. Job information is available for a six month period after creation. Requires that you're the person who ran the job, or have the Is Owner project role. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectId" /> | Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="projectId" /> | Starts a new asynchronous job. This API has two different kinds of endpoint URIs, as this method supports a variety of use cases. * The *Metadata* URI is used for most interactions, as it accepts the job configuration directly. * The *Upload* URI is ONLY for the case when you're sending both a load job configuration and a data stream together. In this case, the Upload URI accepts the job configuration and the data as two distinct multipart MIME parts. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="+jobId, projectId" /> | Requests the deletion of the metadata of a job. This call returns when the job's metadata is deleted. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="+jobId, projectId" /> | Requests that a job be cancelled. This call will return immediately, and the client will need to poll for the job status to see if the cancel completed successfully. Cancelled jobs may still incur costs. |
| <CopyableCode code="query" /> | `EXEC` | <CopyableCode code="projectId" /> | Runs a BigQuery SQL query synchronously and returns query results if the query completes within a specified timeout. |

## `SELECT` examples

Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property.

```sql
SELECT
id,
configuration,
etag,
jobCreationReason,
jobReference,
kind,
principal_subject,
selfLink,
statistics,
status,
user_email
FROM google.bigquery.jobs
WHERE projectId = '{{ projectId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>jobs</code> resource.

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
INSERT INTO google.bigquery.jobs (
projectId,
configuration,
jobReference
)
SELECT 
'{{ projectId }}',
'{{ configuration }}',
'{{ jobReference }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: configuration
      value:
        - name: copy
          value:
            - name: createDisposition
              value: '{{ createDisposition }}'
            - name: destinationEncryptionConfiguration
              value:
                - name: kmsKeyName
                  value: '{{ kmsKeyName }}'
            - name: destinationExpirationTime
              value: '{{ destinationExpirationTime }}'
            - name: destinationTable
              value:
                - name: datasetId
                  value: '{{ datasetId }}'
                - name: projectId
                  value: '{{ projectId }}'
                - name: tableId
                  value: '{{ tableId }}'
            - name: operationType
              value: '{{ operationType }}'
            - name: sourceTables
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: writeDisposition
              value: '{{ writeDisposition }}'
        - name: dryRun
          value: '{{ dryRun }}'
        - name: extract
          value:
            - name: compression
              value: '{{ compression }}'
            - name: destinationFormat
              value: '{{ destinationFormat }}'
            - name: destinationUri
              value: '{{ destinationUri }}'
            - name: destinationUris
              value:
                - name: type
                  value: '{{ type }}'
            - name: fieldDelimiter
              value: '{{ fieldDelimiter }}'
            - name: modelExtractOptions
              value:
                - name: trialId
                  value: '{{ trialId }}'
            - name: printHeader
              value: '{{ printHeader }}'
            - name: sourceModel
              value:
                - name: datasetId
                  value: '{{ datasetId }}'
                - name: modelId
                  value: '{{ modelId }}'
                - name: projectId
                  value: '{{ projectId }}'
            - name: useAvroLogicalTypes
              value: '{{ useAvroLogicalTypes }}'
        - name: jobTimeoutMs
          value: '{{ jobTimeoutMs }}'
        - name: jobType
          value: '{{ jobType }}'
        - name: labels
          value: '{{ labels }}'
        - name: load
          value:
            - name: allowJaggedRows
              value: '{{ allowJaggedRows }}'
            - name: allowQuotedNewlines
              value: '{{ allowQuotedNewlines }}'
            - name: autodetect
              value: '{{ autodetect }}'
            - name: clustering
              value:
                - name: fields
                  value:
                    - name: type
                      value: '{{ type }}'
            - name: columnNameCharacterMap
              value: '{{ columnNameCharacterMap }}'
            - name: connectionProperties
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: copyFilesOnly
              value: '{{ copyFilesOnly }}'
            - name: createDisposition
              value: '{{ createDisposition }}'
            - name: createSession
              value: '{{ createSession }}'
            - name: decimalTargetTypes
              value:
                - name: enum
                  value: '{{ enum }}'
                - name: enumDescriptions
                  value: '{{ enumDescriptions }}'
                - name: type
                  value: '{{ type }}'
            - name: destinationTableProperties
              value:
                - name: description
                  value: '{{ description }}'
                - name: expirationTime
                  value: '{{ expirationTime }}'
                - name: friendlyName
                  value: '{{ friendlyName }}'
                - name: labels
                  value: '{{ labels }}'
            - name: encoding
              value: '{{ encoding }}'
            - name: fieldDelimiter
              value: '{{ fieldDelimiter }}'
            - name: fileSetSpecType
              value: '{{ fileSetSpecType }}'
            - name: hivePartitioningOptions
              value:
                - name: mode
                  value: '{{ mode }}'
                - name: requirePartitionFilter
                  value: '{{ requirePartitionFilter }}'
                - name: sourceUriPrefix
                  value: '{{ sourceUriPrefix }}'
            - name: ignoreUnknownValues
              value: '{{ ignoreUnknownValues }}'
            - name: jsonExtension
              value: '{{ jsonExtension }}'
            - name: maxBadRecords
              value: '{{ maxBadRecords }}'
            - name: nullMarker
              value: '{{ nullMarker }}'
            - name: parquetOptions
              value:
                - name: enableListInference
                  value: '{{ enableListInference }}'
                - name: enumAsString
                  value: '{{ enumAsString }}'
                - name: mapTargetType
                  value: '{{ mapTargetType }}'
            - name: preserveAsciiControlCharacters
              value: '{{ preserveAsciiControlCharacters }}'
            - name: projectionFields
              value:
                - name: type
                  value: '{{ type }}'
            - name: quote
              value: '{{ quote }}'
            - name: rangePartitioning
              value:
                - name: field
                  value: '{{ field }}'
                - name: range
                  value:
                    - name: end
                      value: '{{ end }}'
                    - name: interval
                      value: '{{ interval }}'
                    - name: start
                      value: '{{ start }}'
            - name: referenceFileSchemaUri
              value: '{{ referenceFileSchemaUri }}'
            - name: schema
              value:
                - name: fields
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
                - name: foreignTypeInfo
                  value:
                    - name: typeSystem
                      value: '{{ typeSystem }}'
            - name: schemaInline
              value: '{{ schemaInline }}'
            - name: schemaInlineFormat
              value: '{{ schemaInlineFormat }}'
            - name: schemaUpdateOptions
              value:
                - name: type
                  value: '{{ type }}'
            - name: skipLeadingRows
              value: '{{ skipLeadingRows }}'
            - name: sourceFormat
              value: '{{ sourceFormat }}'
            - name: sourceUris
              value:
                - name: type
                  value: '{{ type }}'
            - name: timePartitioning
              value:
                - name: expirationMs
                  value: '{{ expirationMs }}'
                - name: field
                  value: '{{ field }}'
                - name: requirePartitionFilter
                  value: '{{ requirePartitionFilter }}'
                - name: type
                  value: '{{ type }}'
            - name: useAvroLogicalTypes
              value: '{{ useAvroLogicalTypes }}'
            - name: writeDisposition
              value: '{{ writeDisposition }}'
        - name: query
          value:
            - name: allowLargeResults
              value: '{{ allowLargeResults }}'
            - name: connectionProperties
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: continuous
              value: '{{ continuous }}'
            - name: createDisposition
              value: '{{ createDisposition }}'
            - name: createSession
              value: '{{ createSession }}'
            - name: defaultDataset
              value:
                - name: datasetId
                  value: '{{ datasetId }}'
                - name: projectId
                  value: '{{ projectId }}'
            - name: flattenResults
              value: '{{ flattenResults }}'
            - name: maximumBillingTier
              value: '{{ maximumBillingTier }}'
            - name: maximumBytesBilled
              value: '{{ maximumBytesBilled }}'
            - name: parameterMode
              value: '{{ parameterMode }}'
            - name: preserveNulls
              value: '{{ preserveNulls }}'
            - name: priority
              value: '{{ priority }}'
            - name: query
              value: '{{ query }}'
            - name: queryParameters
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: schemaUpdateOptions
              value:
                - name: type
                  value: '{{ type }}'
            - name: scriptOptions
              value:
                - name: keyResultStatement
                  value: '{{ keyResultStatement }}'
                - name: statementByteBudget
                  value: '{{ statementByteBudget }}'
                - name: statementTimeoutMs
                  value: '{{ statementTimeoutMs }}'
            - name: tableDefinitions
              value: '{{ tableDefinitions }}'
            - name: useLegacySql
              value: '{{ useLegacySql }}'
            - name: useQueryCache
              value: '{{ useQueryCache }}'
            - name: userDefinedFunctionResources
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: writeDisposition
              value: '{{ writeDisposition }}'
    - name: jobReference
      value:
        - name: jobId
          value: '{{ jobId }}'
        - name: location
          value: '{{ location }}'
        - name: projectId
          value: '{{ projectId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigquery.jobs
WHERE +jobId = '{{ +jobId }}'
AND projectId = '{{ projectId }}';
```
