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
| <CopyableCode code="jobCreationReason" /> | `object` | Reason about why a Job was created from a [`jobs.query`](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query) method when used with `JOB_CREATION_OPTIONAL` Job creation mode. For [`jobs.insert`](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert) method calls it will always be `REQUESTED`. [Preview](https://cloud.google.com/products/#product-launch-stages) |
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
              value: string
            - name: destinationEncryptionConfiguration
              value:
                - name: kmsKeyName
                  value: string
            - name: destinationExpirationTime
              value: string
            - name: destinationTable
              value:
                - name: datasetId
                  value: string
                - name: projectId
                  value: string
                - name: tableId
                  value: string
            - name: operationType
              value: string
            - name: sourceTables
              value:
                - - name: datasetId
                    value: string
                  - name: projectId
                    value: string
                  - name: tableId
                    value: string
            - name: writeDisposition
              value: string
        - name: dryRun
          value: boolean
        - name: extract
          value:
            - name: compression
              value: string
            - name: destinationFormat
              value: string
            - name: destinationUri
              value: string
            - name: destinationUris
              value:
                - string
            - name: fieldDelimiter
              value: string
            - name: modelExtractOptions
              value:
                - name: trialId
                  value: string
            - name: printHeader
              value: boolean
            - name: sourceModel
              value:
                - name: datasetId
                  value: string
                - name: modelId
                  value: string
                - name: projectId
                  value: string
            - name: useAvroLogicalTypes
              value: boolean
        - name: jobTimeoutMs
          value: string
        - name: jobType
          value: string
        - name: labels
          value: object
        - name: load
          value:
            - name: allowJaggedRows
              value: boolean
            - name: allowQuotedNewlines
              value: boolean
            - name: autodetect
              value: boolean
            - name: clustering
              value:
                - name: fields
                  value:
                    - string
            - name: columnNameCharacterMap
              value: string
            - name: connectionProperties
              value:
                - - name: key
                    value: string
                  - name: value
                    value: string
            - name: copyFilesOnly
              value: boolean
            - name: createDisposition
              value: string
            - name: createSession
              value: boolean
            - name: decimalTargetTypes
              value:
                - string
            - name: destinationTableProperties
              value:
                - name: description
                  value: string
                - name: expirationTime
                  value: string
                - name: friendlyName
                  value: string
                - name: labels
                  value: object
            - name: encoding
              value: string
            - name: fieldDelimiter
              value: string
            - name: fileSetSpecType
              value: string
            - name: hivePartitioningOptions
              value:
                - name: fields
                  value:
                    - string
                - name: mode
                  value: string
                - name: requirePartitionFilter
                  value: boolean
                - name: sourceUriPrefix
                  value: string
            - name: ignoreUnknownValues
              value: boolean
            - name: jsonExtension
              value: string
            - name: maxBadRecords
              value: integer
            - name: nullMarker
              value: string
            - name: parquetOptions
              value:
                - name: enableListInference
                  value: boolean
                - name: enumAsString
                  value: boolean
                - name: mapTargetType
                  value: string
            - name: preserveAsciiControlCharacters
              value: boolean
            - name: projectionFields
              value:
                - string
            - name: quote
              value: string
            - name: rangePartitioning
              value:
                - name: field
                  value: string
                - name: range
                  value:
                    - name: end
                      value: string
                    - name: interval
                      value: string
                    - name: start
                      value: string
            - name: referenceFileSchemaUri
              value: string
            - name: schema
              value:
                - name: fields
                  value:
                    - - name: categories
                        value:
                          - name: names
                            value:
                              - string
                      - name: collation
                        value: string
                      - name: dataPolicies
                        value:
                          - - name: name
                              value: string
                      - name: defaultValueExpression
                        value: string
                      - name: description
                        value: string
                      - name: fields
                        value:
                          - - name: categories
                              value:
                                - name: names
                                  value:
                                    - string
                            - name: collation
                              value: string
                            - name: dataPolicies
                              value:
                                - - name: name
                                    value: string
                            - name: defaultValueExpression
                              value: string
                            - name: description
                              value: string
                            - name: fields
                              value:
                                - - name: categories
                                    value:
                                      - name: names
                                        value:
                                          - string
                                  - name: collation
                                    value: string
                                  - name: dataPolicies
                                    value:
                                      - - name: name
                                          value: string
                                  - name: defaultValueExpression
                                    value: string
                                  - name: description
                                    value: string
                                  - name: fields
                                    value:
                                      - - name: categories
                                          value:
                                            - name: names
                                              value:
                                                - string
                                        - name: collation
                                          value: string
                                        - name: dataPolicies
                                          value:
                                            - - name: name
                                                value: string
                                        - name: defaultValueExpression
                                          value: string
                                        - name: description
                                          value: string
                                        - name: fields
                                          value:
                                            - - name: categories
                                                value:
                                                  - name: names
                                                    value:
                                                      - string
                                              - name: collation
                                                value: string
                                              - name: dataPolicies
                                                value:
                                                  - - name: name
                                                      value: string
                                              - name: defaultValueExpression
                                                value: string
                                              - name: description
                                                value: string
                                              - name: fields
                                                value:
                                                  - - name: categories
                                                      value:
                                                        - name: names
                                                          value:
                                                            - string
                                                    - name: collation
                                                      value: string
                                                    - name: dataPolicies
                                                      value:
                                                        - - name: name
                                                            value: string
                                                    - name: defaultValueExpression
                                                      value: string
                                                    - name: description
                                                      value: string
                                                    - name: fields
                                                      value:
                                                        - - name: categories
                                                            value: []
                                                          - name: collation
                                                            value: string
                                                          - name: dataPolicies
                                                            value:
                                                              - []
                                                          - name: defaultValueExpression
                                                            value: string
                                                          - name: description
                                                            value: string
                                                          - name: fields
                                                            value:
                                                              - []
                                                          - name: foreignTypeDefinition
                                                            value: string
                                                          - name: maxLength
                                                            value: string
                                                          - name: mode
                                                            value: string
                                                          - name: name
                                                            value: string
                                                          - name: policyTags
                                                            value: []
                                                          - name: precision
                                                            value: string
                                                          - name: rangeElementType
                                                            value: []
                                                          - name: roundingMode
                                                            value: string
                                                          - name: scale
                                                            value: string
                                                          - name: type
                                                            value: string
                                                    - name: foreignTypeDefinition
                                                      value: string
                                                    - name: maxLength
                                                      value: string
                                                    - name: mode
                                                      value: string
                                                    - name: name
                                                      value: string
                                                    - name: policyTags
                                                      value:
                                                        - name: names
                                                          value:
                                                            - string
                                                    - name: precision
                                                      value: string
                                                    - name: rangeElementType
                                                      value:
                                                        - name: type
                                                          value: string
                                                    - name: roundingMode
                                                      value: string
                                                    - name: scale
                                                      value: string
                                                    - name: type
                                                      value: string
                                              - name: foreignTypeDefinition
                                                value: string
                                              - name: maxLength
                                                value: string
                                              - name: mode
                                                value: string
                                              - name: name
                                                value: string
                                              - name: policyTags
                                                value:
                                                  - name: names
                                                    value:
                                                      - string
                                              - name: precision
                                                value: string
                                              - name: rangeElementType
                                                value:
                                                  - name: type
                                                    value: string
                                              - name: roundingMode
                                                value: string
                                              - name: scale
                                                value: string
                                              - name: type
                                                value: string
                                        - name: foreignTypeDefinition
                                          value: string
                                        - name: maxLength
                                          value: string
                                        - name: mode
                                          value: string
                                        - name: name
                                          value: string
                                        - name: policyTags
                                          value:
                                            - name: names
                                              value:
                                                - string
                                        - name: precision
                                          value: string
                                        - name: rangeElementType
                                          value:
                                            - name: type
                                              value: string
                                        - name: roundingMode
                                          value: string
                                        - name: scale
                                          value: string
                                        - name: type
                                          value: string
                                  - name: foreignTypeDefinition
                                    value: string
                                  - name: maxLength
                                    value: string
                                  - name: mode
                                    value: string
                                  - name: name
                                    value: string
                                  - name: policyTags
                                    value:
                                      - name: names
                                        value:
                                          - string
                                  - name: precision
                                    value: string
                                  - name: rangeElementType
                                    value:
                                      - name: type
                                        value: string
                                  - name: roundingMode
                                    value: string
                                  - name: scale
                                    value: string
                                  - name: type
                                    value: string
                            - name: foreignTypeDefinition
                              value: string
                            - name: maxLength
                              value: string
                            - name: mode
                              value: string
                            - name: name
                              value: string
                            - name: policyTags
                              value:
                                - name: names
                                  value:
                                    - string
                            - name: precision
                              value: string
                            - name: rangeElementType
                              value:
                                - name: type
                                  value: string
                            - name: roundingMode
                              value: string
                            - name: scale
                              value: string
                            - name: type
                              value: string
                      - name: foreignTypeDefinition
                        value: string
                      - name: maxLength
                        value: string
                      - name: mode
                        value: string
                      - name: name
                        value: string
                      - name: policyTags
                        value:
                          - name: names
                            value:
                              - string
                      - name: precision
                        value: string
                      - name: rangeElementType
                        value:
                          - name: type
                            value: string
                      - name: roundingMode
                        value: string
                      - name: scale
                        value: string
                      - name: type
                        value: string
                - name: foreignTypeInfo
                  value:
                    - name: typeSystem
                      value: string
            - name: schemaInline
              value: string
            - name: schemaInlineFormat
              value: string
            - name: schemaUpdateOptions
              value:
                - string
            - name: skipLeadingRows
              value: integer
            - name: sourceFormat
              value: string
            - name: sourceUris
              value:
                - string
            - name: timePartitioning
              value:
                - name: expirationMs
                  value: string
                - name: field
                  value: string
                - name: requirePartitionFilter
                  value: boolean
                - name: type
                  value: string
            - name: useAvroLogicalTypes
              value: boolean
            - name: writeDisposition
              value: string
        - name: query
          value:
            - name: allowLargeResults
              value: boolean
            - name: connectionProperties
              value:
                - - name: key
                    value: string
                  - name: value
                    value: string
            - name: continuous
              value: boolean
            - name: createDisposition
              value: string
            - name: createSession
              value: boolean
            - name: defaultDataset
              value:
                - name: datasetId
                  value: string
                - name: projectId
                  value: string
            - name: flattenResults
              value: boolean
            - name: maximumBillingTier
              value: integer
            - name: maximumBytesBilled
              value: string
            - name: parameterMode
              value: string
            - name: preserveNulls
              value: boolean
            - name: priority
              value: string
            - name: query
              value: string
            - name: queryParameters
              value:
                - - name: name
                    value: string
                  - name: parameterType
                    value:
                      - name: structTypes
                        value:
                          - - name: description
                              value: string
                            - name: name
                              value: string
                      - name: type
                        value: string
                  - name: parameterValue
                    value:
                      - name: arrayValues
                        value:
                          - - name: arrayValues
                              value:
                                - - name: arrayValues
                                    value:
                                      - - name: arrayValues
                                          value:
                                            - - name: arrayValues
                                                value:
                                                  - - name: arrayValues
                                                      value:
                                                        - - name: arrayValues
                                                            value:
                                                              - []
                                                          - name: rangeValue
                                                            value: []
                                                          - name: structValues
                                                            value: object
                                                          - name: value
                                                            value: string
                                                    - name: structValues
                                                      value: object
                                                    - name: value
                                                      value: string
                                              - name: structValues
                                                value: object
                                              - name: value
                                                value: string
                                        - name: structValues
                                          value: object
                                        - name: value
                                          value: string
                                  - name: structValues
                                    value: object
                                  - name: value
                                    value: string
                            - name: structValues
                              value: object
                            - name: value
                              value: string
                      - name: structValues
                        value: object
                      - name: value
                        value: string
            - name: schemaUpdateOptions
              value:
                - string
            - name: scriptOptions
              value:
                - name: keyResultStatement
                  value: string
                - name: statementByteBudget
                  value: string
                - name: statementTimeoutMs
                  value: string
            - name: systemVariables
              value:
                - name: types
                  value: object
                - name: values
                  value: object
            - name: tableDefinitions
              value: object
            - name: useLegacySql
              value: boolean
            - name: useQueryCache
              value: boolean
            - name: userDefinedFunctionResources
              value:
                - - name: inlineCode
                    value: string
                  - name: resourceUri
                    value: string
            - name: writeDisposition
              value: string
    - name: etag
      value: string
    - name: id
      value: string
    - name: jobCreationReason
      value:
        - name: code
          value: string
    - name: jobReference
      value:
        - name: jobId
          value: string
        - name: location
          value: string
        - name: projectId
          value: string
    - name: kind
      value: string
    - name: principal_subject
      value: string
    - name: selfLink
      value: string
    - name: statistics
      value:
        - name: completionRatio
          value: number
        - name: copy
          value:
            - name: copiedLogicalBytes
              value: string
            - name: copiedRows
              value: string
        - name: creationTime
          value: string
        - name: dataMaskingStatistics
          value:
            - name: dataMaskingApplied
              value: boolean
        - name: edition
          value: string
        - name: endTime
          value: string
        - name: extract
          value:
            - name: destinationUriFileCounts
              value:
                - string
            - name: inputBytes
              value: string
            - name: timeline
              value:
                - - name: activeUnits
                    value: string
                  - name: completedUnits
                    value: string
                  - name: elapsedMs
                    value: string
                  - name: estimatedRunnableUnits
                    value: string
                  - name: pendingUnits
                    value: string
                  - name: totalSlotMs
                    value: string
        - name: finalExecutionDurationMs
          value: string
        - name: load
          value:
            - name: badRecords
              value: string
            - name: inputFileBytes
              value: string
            - name: inputFiles
              value: string
            - name: outputBytes
              value: string
            - name: outputRows
              value: string
            - name: timeline
              value:
                - - name: activeUnits
                    value: string
                  - name: completedUnits
                    value: string
                  - name: elapsedMs
                    value: string
                  - name: estimatedRunnableUnits
                    value: string
                  - name: pendingUnits
                    value: string
                  - name: totalSlotMs
                    value: string
        - name: numChildJobs
          value: string
        - name: parentJobId
          value: string
        - name: query
          value:
            - name: biEngineStatistics
              value:
                - name: accelerationMode
                  value: string
                - name: biEngineMode
                  value: string
                - name: biEngineReasons
                  value:
                    - - name: code
                        value: string
                      - name: message
                        value: string
            - name: billingTier
              value: integer
            - name: cacheHit
              value: boolean
            - name: ddlAffectedRowAccessPolicyCount
              value: string
            - name: ddlOperationPerformed
              value: string
            - name: ddlTargetRoutine
              value:
                - name: datasetId
                  value: string
                - name: projectId
                  value: string
                - name: routineId
                  value: string
            - name: ddlTargetRowAccessPolicy
              value:
                - name: datasetId
                  value: string
                - name: policyId
                  value: string
                - name: projectId
                  value: string
                - name: tableId
                  value: string
            - name: dmlStats
              value:
                - name: deletedRowCount
                  value: string
                - name: insertedRowCount
                  value: string
                - name: updatedRowCount
                  value: string
            - name: estimatedBytesProcessed
              value: string
            - name: exportDataStatistics
              value:
                - name: fileCount
                  value: string
                - name: rowCount
                  value: string
            - name: externalServiceCosts
              value:
                - - name: bytesBilled
                    value: string
                  - name: bytesProcessed
                    value: string
                  - name: externalService
                    value: string
                  - name: reservedSlotCount
                    value: string
                  - name: slotMs
                    value: string
            - name: loadQueryStatistics
              value:
                - name: badRecords
                  value: string
                - name: bytesTransferred
                  value: string
                - name: inputFileBytes
                  value: string
                - name: inputFiles
                  value: string
                - name: outputBytes
                  value: string
                - name: outputRows
                  value: string
            - name: materializedViewStatistics
              value:
                - name: materializedView
                  value:
                    - - name: chosen
                        value: boolean
                      - name: estimatedBytesSaved
                        value: string
                      - name: rejectedReason
                        value: string
            - name: metadataCacheStatistics
              value:
                - name: tableMetadataCacheUsage
                  value:
                    - - name: explanation
                        value: string
                      - name: staleness
                        value: string
                      - name: tableType
                        value: string
                      - name: unusedReason
                        value: string
            - name: mlStatistics
              value:
                - name: hparamTrials
                  value:
                    - - name: endTimeMs
                        value: string
                      - name: errorMessage
                        value: string
                      - name: evalLoss
                        value: number
                      - name: evaluationMetrics
                        value:
                          - name: arimaForecastingMetrics
                            value:
                              - name: arimaFittingMetrics
                                value:
                                  - - name: aic
                                      value: number
                                    - name: logLikelihood
                                      value: number
                                    - name: variance
                                      value: number
                              - name: arimaSingleModelForecastingMetrics
                                value:
                                  - - name: arimaFittingMetrics
                                      value:
                                        - name: aic
                                          value: number
                                        - name: logLikelihood
                                          value: number
                                        - name: variance
                                          value: number
                                    - name: hasDrift
                                      value: boolean
                                    - name: hasHolidayEffect
                                      value: boolean
                                    - name: hasSpikesAndDips
                                      value: boolean
                                    - name: hasStepChanges
                                      value: boolean
                                    - name: nonSeasonalOrder
                                      value:
                                        - name: d
                                          value: string
                                        - name: p
                                          value: string
                                        - name: q
                                          value: string
                                    - name: seasonalPeriods
                                      value:
                                        - string
                                    - name: timeSeriesId
                                      value: string
                                    - name: timeSeriesIds
                                      value:
                                        - string
                              - name: hasDrift
                                value:
                                  - boolean
                              - name: nonSeasonalOrder
                                value:
                                  - - name: d
                                      value: string
                                    - name: p
                                      value: string
                                    - name: q
                                      value: string
                              - name: seasonalPeriods
                                value:
                                  - string
                              - name: timeSeriesId
                                value:
                                  - string
                          - name: binaryClassificationMetrics
                            value:
                              - name: aggregateClassificationMetrics
                                value:
                                  - name: accuracy
                                    value: number
                                  - name: f1Score
                                    value: number
                                  - name: logLoss
                                    value: number
                                  - name: precision
                                    value: number
                                  - name: recall
                                    value: number
                                  - name: rocAuc
                                    value: number
                                  - name: threshold
                                    value: number
                              - name: binaryConfusionMatrixList
                                value:
                                  - - name: accuracy
                                      value: number
                                    - name: f1Score
                                      value: number
                                    - name: falseNegatives
                                      value: string
                                    - name: falsePositives
                                      value: string
                                    - name: positiveClassThreshold
                                      value: number
                                    - name: precision
                                      value: number
                                    - name: recall
                                      value: number
                                    - name: trueNegatives
                                      value: string
                                    - name: truePositives
                                      value: string
                              - name: negativeLabel
                                value: string
                              - name: positiveLabel
                                value: string
                          - name: clusteringMetrics
                            value:
                              - name: clusters
                                value:
                                  - - name: centroidId
                                      value: string
                                    - name: count
                                      value: string
                                    - name: featureValues
                                      value:
                                        - - name: categoricalValue
                                            value:
                                              - name: categoryCounts
                                                value:
                                                  - - name: category
                                                      value: string
                                                    - name: count
                                                      value: string
                                          - name: featureColumn
                                            value: string
                                          - name: numericalValue
                                            value: number
                              - name: daviesBouldinIndex
                                value: number
                              - name: meanSquaredDistance
                                value: number
                          - name: dimensionalityReductionMetrics
                            value:
                              - name: totalExplainedVarianceRatio
                                value: number
                          - name: multiClassClassificationMetrics
                            value:
                              - name: confusionMatrixList
                                value:
                                  - - name: confidenceThreshold
                                      value: number
                                    - name: rows
                                      value:
                                        - - name: actualLabel
                                            value: string
                                          - name: entries
                                            value:
                                              - - name: itemCount
                                                  value: string
                                                - name: predictedLabel
                                                  value: string
                          - name: rankingMetrics
                            value:
                              - name: averageRank
                                value: number
                              - name: meanAveragePrecision
                                value: number
                              - name: meanSquaredError
                                value: number
                              - name: normalizedDiscountedCumulativeGain
                                value: number
                          - name: regressionMetrics
                            value:
                              - name: meanAbsoluteError
                                value: number
                              - name: meanSquaredError
                                value: number
                              - name: meanSquaredLogError
                                value: number
                              - name: medianAbsoluteError
                                value: number
                              - name: rSquared
                                value: number
                      - name: hparams
                        value:
                          - name: activationFn
                            value: string
                          - name: adjustStepChanges
                            value: boolean
                          - name: approxGlobalFeatureContrib
                            value: boolean
                          - name: autoArima
                            value: boolean
                          - name: autoArimaMaxOrder
                            value: string
                          - name: autoArimaMinOrder
                            value: string
                          - name: autoClassWeights
                            value: boolean
                          - name: batchSize
                            value: string
                          - name: boosterType
                            value: string
                          - name: budgetHours
                            value: number
                          - name: calculatePValues
                            value: boolean
                          - name: categoryEncodingMethod
                            value: string
                          - name: cleanSpikesAndDips
                            value: boolean
                          - name: colorSpace
                            value: string
                          - name: colsampleBylevel
                            value: number
                          - name: colsampleBynode
                            value: number
                          - name: colsampleBytree
                            value: number
                          - name: dartNormalizeType
                            value: string
                          - name: dataFrequency
                            value: string
                          - name: dataSplitColumn
                            value: string
                          - name: dataSplitEvalFraction
                            value: number
                          - name: dataSplitMethod
                            value: string
                          - name: decomposeTimeSeries
                            value: boolean
                          - name: distanceType
                            value: string
                          - name: dropout
                            value: number
                          - name: earlyStop
                            value: boolean
                          - name: enableGlobalExplain
                            value: boolean
                          - name: feedbackType
                            value: string
                          - name: fitIntercept
                            value: boolean
                          - name: hiddenUnits
                            value:
                              - string
                          - name: holidayRegion
                            value: string
                          - name: holidayRegions
                            value:
                              - string
                          - name: horizon
                            value: string
                          - name: hparamTuningObjectives
                            value:
                              - string
                          - name: includeDrift
                            value: boolean
                          - name: initialLearnRate
                            value: number
                          - name: inputLabelColumns
                            value:
                              - string
                          - name: instanceWeightColumn
                            value: string
                          - name: integratedGradientsNumSteps
                            value: string
                          - name: itemColumn
                            value: string
                          - name: kmeansInitializationColumn
                            value: string
                          - name: kmeansInitializationMethod
                            value: string
                          - name: l1RegActivation
                            value: number
                          - name: l1Regularization
                            value: number
                          - name: l2Regularization
                            value: number
                          - name: labelClassWeights
                            value: object
                          - name: learnRate
                            value: number
                          - name: learnRateStrategy
                            value: string
                          - name: lossType
                            value: string
                          - name: maxIterations
                            value: string
                          - name: maxParallelTrials
                            value: string
                          - name: maxTimeSeriesLength
                            value: string
                          - name: maxTreeDepth
                            value: string
                          - name: minRelativeProgress
                            value: number
                          - name: minSplitLoss
                            value: number
                          - name: minTimeSeriesLength
                            value: string
                          - name: minTreeChildWeight
                            value: string
                          - name: modelRegistry
                            value: string
                          - name: modelUri
                            value: string
                          - name: numClusters
                            value: string
                          - name: numFactors
                            value: string
                          - name: numParallelTree
                            value: string
                          - name: numPrincipalComponents
                            value: string
                          - name: numTrials
                            value: string
                          - name: optimizationStrategy
                            value: string
                          - name: optimizer
                            value: string
                          - name: pcaExplainedVarianceRatio
                            value: number
                          - name: pcaSolver
                            value: string
                          - name: sampledShapleyNumPaths
                            value: string
                          - name: scaleFeatures
                            value: boolean
                          - name: standardizeFeatures
                            value: boolean
                          - name: subsample
                            value: number
                          - name: tfVersion
                            value: string
                          - name: timeSeriesDataColumn
                            value: string
                          - name: timeSeriesIdColumn
                            value: string
                          - name: timeSeriesIdColumns
                            value:
                              - string
                          - name: timeSeriesLengthFraction
                            value: number
                          - name: timeSeriesTimestampColumn
                            value: string
                          - name: treeMethod
                            value: string
                          - name: trendSmoothingWindowSize
                            value: string
                          - name: userColumn
                            value: string
                          - name: vertexAiModelVersionAliases
                            value:
                              - string
                          - name: walsAlpha
                            value: number
                          - name: warmStart
                            value: boolean
                          - name: xgboostVersion
                            value: string
                      - name: startTimeMs
                        value: string
                      - name: status
                        value: string
                      - name: trainingLoss
                        value: number
                      - name: trialId
                        value: string
                - name: iterationResults
                  value:
                    - - name: arimaResult
                        value:
                          - name: arimaModelInfo
                            value:
                              - - name: arimaCoefficients
                                  value:
                                    - name: autoRegressiveCoefficients
                                      value:
                                        - number
                                    - name: interceptCoefficient
                                      value: number
                                    - name: movingAverageCoefficients
                                      value:
                                        - number
                                - name: hasDrift
                                  value: boolean
                                - name: hasHolidayEffect
                                  value: boolean
                                - name: hasSpikesAndDips
                                  value: boolean
                                - name: hasStepChanges
                                  value: boolean
                                - name: seasonalPeriods
                                  value:
                                    - string
                                - name: timeSeriesId
                                  value: string
                                - name: timeSeriesIds
                                  value:
                                    - string
                          - name: seasonalPeriods
                            value:
                              - string
                      - name: clusterInfos
                        value:
                          - - name: centroidId
                              value: string
                            - name: clusterRadius
                              value: number
                            - name: clusterSize
                              value: string
                      - name: durationMs
                        value: string
                      - name: evalLoss
                        value: number
                      - name: index
                        value: integer
                      - name: learnRate
                        value: number
                      - name: principalComponentInfos
                        value:
                          - - name: cumulativeExplainedVarianceRatio
                              value: number
                            - name: explainedVariance
                              value: number
                            - name: explainedVarianceRatio
                              value: number
                            - name: principalComponentId
                              value: string
                      - name: trainingLoss
                        value: number
                - name: maxIterations
                  value: string
                - name: modelType
                  value: string
                - name: trainingType
                  value: string
            - name: modelTraining
              value:
                - name: currentIteration
                  value: integer
                - name: expectedTotalIterations
                  value: string
            - name: modelTrainingCurrentIteration
              value: integer
            - name: modelTrainingExpectedTotalIteration
              value: string
            - name: numDmlAffectedRows
              value: string
            - name: performanceInsights
              value:
                - name: avgPreviousExecutionMs
                  value: string
                - name: stagePerformanceChangeInsights
                  value:
                    - - name: inputDataChange
                        value:
                          - name: recordsReadDiffPercentage
                            value: number
                      - name: stageId
                        value: string
                - name: stagePerformanceStandaloneInsights
                  value:
                    - - name: biEngineReasons
                        value:
                          - - name: code
                              value: string
                            - name: message
                              value: string
                      - name: highCardinalityJoins
                        value:
                          - - name: leftRows
                              value: string
                            - name: outputRows
                              value: string
                            - name: rightRows
                              value: string
                            - name: stepIndex
                              value: integer
                      - name: insufficientShuffleQuota
                        value: boolean
                      - name: partitionSkew
                        value:
                          - name: skewSources
                            value:
                              - - name: stageId
                                  value: string
                      - name: slotContention
                        value: boolean
                      - name: stageId
                        value: string
            - name: queryInfo
              value:
                - name: optimizationDetails
                  value: object
            - name: queryPlan
              value:
                - - name: completedParallelInputs
                    value: string
                  - name: computeMode
                    value: string
                  - name: computeMsAvg
                    value: string
                  - name: computeMsMax
                    value: string
                  - name: computeRatioAvg
                    value: number
                  - name: computeRatioMax
                    value: number
                  - name: endMs
                    value: string
                  - name: id
                    value: string
                  - name: inputStages
                    value:
                      - string
                  - name: name
                    value: string
                  - name: parallelInputs
                    value: string
                  - name: readMsAvg
                    value: string
                  - name: readMsMax
                    value: string
                  - name: readRatioAvg
                    value: number
                  - name: readRatioMax
                    value: number
                  - name: recordsRead
                    value: string
                  - name: recordsWritten
                    value: string
                  - name: shuffleOutputBytes
                    value: string
                  - name: shuffleOutputBytesSpilled
                    value: string
                  - name: slotMs
                    value: string
                  - name: startMs
                    value: string
                  - name: status
                    value: string
                  - name: steps
                    value:
                      - - name: kind
                          value: string
                        - name: substeps
                          value:
                            - string
                  - name: waitMsAvg
                    value: string
                  - name: waitMsMax
                    value: string
                  - name: waitRatioAvg
                    value: number
                  - name: waitRatioMax
                    value: number
                  - name: writeMsAvg
                    value: string
                  - name: writeMsMax
                    value: string
                  - name: writeRatioAvg
                    value: number
                  - name: writeRatioMax
                    value: number
            - name: referencedRoutines
              value:
                - - name: datasetId
                    value: string
                  - name: projectId
                    value: string
                  - name: routineId
                    value: string
            - name: referencedTables
              value:
                - - name: datasetId
                    value: string
                  - name: projectId
                    value: string
                  - name: tableId
                    value: string
            - name: reservationUsage
              value:
                - - name: name
                    value: string
                  - name: slotMs
                    value: string
            - name: searchStatistics
              value:
                - name: indexUnusedReasons
                  value:
                    - - name: code
                        value: string
                      - name: indexName
                        value: string
                      - name: message
                        value: string
                - name: indexUsageMode
                  value: string
            - name: sparkStatistics
              value:
                - name: endpoints
                  value: object
                - name: gcsStagingBucket
                  value: string
                - name: kmsKeyName
                  value: string
                - name: loggingInfo
                  value:
                    - name: projectId
                      value: string
                    - name: resourceType
                      value: string
                - name: sparkJobId
                  value: string
                - name: sparkJobLocation
                  value: string
            - name: statementType
              value: string
            - name: timeline
              value:
                - - name: activeUnits
                    value: string
                  - name: completedUnits
                    value: string
                  - name: elapsedMs
                    value: string
                  - name: estimatedRunnableUnits
                    value: string
                  - name: pendingUnits
                    value: string
                  - name: totalSlotMs
                    value: string
            - name: totalBytesBilled
              value: string
            - name: totalBytesProcessed
              value: string
            - name: totalBytesProcessedAccuracy
              value: string
            - name: totalPartitionsProcessed
              value: string
            - name: totalSlotMs
              value: string
            - name: transferredBytes
              value: string
            - name: undeclaredQueryParameters
              value:
                - - name: name
                    value: string
            - name: vectorSearchStatistics
              value:
                - name: indexUnusedReasons
                  value:
                    - - name: code
                        value: string
                      - name: indexName
                        value: string
                      - name: message
                        value: string
                - name: indexUsageMode
                  value: string
        - name: quotaDeferments
          value:
            - string
        - name: reservationUsage
          value:
            - - name: name
                value: string
              - name: slotMs
                value: string
        - name: reservation_id
          value: string
        - name: rowLevelSecurityStatistics
          value:
            - name: rowLevelSecurityApplied
              value: boolean
        - name: scriptStatistics
          value:
            - name: evaluationKind
              value: string
            - name: stackFrames
              value:
                - - name: endColumn
                    value: integer
                  - name: endLine
                    value: integer
                  - name: procedureId
                    value: string
                  - name: startColumn
                    value: integer
                  - name: startLine
                    value: integer
                  - name: text
                    value: string
        - name: sessionInfo
          value:
            - name: sessionId
              value: string
        - name: startTime
          value: string
        - name: totalBytesProcessed
          value: string
        - name: totalSlotMs
          value: string
        - name: transactionInfo
          value:
            - name: transactionId
              value: string
    - name: status
      value:
        - name: errorResult
          value:
            - name: debugInfo
              value: string
            - name: location
              value: string
            - name: message
              value: string
            - name: reason
              value: string
        - name: errors
          value:
            - - name: debugInfo
                value: string
              - name: location
                value: string
              - name: message
                value: string
              - name: reason
                value: string
        - name: state
          value: string
    - name: user_email
      value: string

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
