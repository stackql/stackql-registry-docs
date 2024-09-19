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
configuration:
  copy:
    createDisposition: string
    destinationEncryptionConfiguration:
      kmsKeyName: string
    destinationExpirationTime: string
    destinationTable:
      datasetId: string
      projectId: string
      tableId: string
    operationType: string
    sourceTables:
      - datasetId: string
        projectId: string
        tableId: string
    writeDisposition: string
  dryRun: boolean
  extract:
    compression: string
    destinationFormat: string
    destinationUri: string
    destinationUris:
      - type: string
    fieldDelimiter: string
    modelExtractOptions:
      trialId: string
    printHeader: boolean
    sourceModel:
      datasetId: string
      modelId: string
      projectId: string
    useAvroLogicalTypes: boolean
  jobTimeoutMs: string
  jobType: string
  labels: object
  load:
    allowJaggedRows: boolean
    allowQuotedNewlines: boolean
    autodetect: boolean
    clustering:
      fields:
        - type: string
    columnNameCharacterMap: string
    connectionProperties:
      - key: string
        value: string
    copyFilesOnly: boolean
    createDisposition: string
    createSession: boolean
    decimalTargetTypes:
      - enum: string
        enumDescriptions: string
        type: string
    destinationTableProperties:
      description: string
      expirationTime: string
      friendlyName: string
      labels: object
    encoding: string
    fieldDelimiter: string
    fileSetSpecType: string
    hivePartitioningOptions:
      fields:
        - type: string
      mode: string
      requirePartitionFilter: boolean
      sourceUriPrefix: string
    ignoreUnknownValues: boolean
    jsonExtension: string
    maxBadRecords: integer
    nullMarker: string
    parquetOptions:
      enableListInference: boolean
      enumAsString: boolean
      mapTargetType: string
    preserveAsciiControlCharacters: boolean
    projectionFields:
      - type: string
    quote: string
    rangePartitioning:
      field: string
      range:
        end: string
        interval: string
        start: string
    referenceFileSchemaUri: string
    schema:
      fields:
        - categories:
            names:
              - type: string
          collation: string
          dataPolicies:
            - name: string
          defaultValueExpression: string
          description: string
          fields:
            - categories:
                names:
                  - type: string
              collation: string
              dataPolicies:
                - name: string
              defaultValueExpression: string
              description: string
              fields:
                - categories:
                    names:
                      - type: string
                  collation: string
                  dataPolicies:
                    - name: string
                  defaultValueExpression: string
                  description: string
                  fields:
                    - categories:
                        names:
                          - type: string
                      collation: string
                      dataPolicies:
                        - name: string
                      defaultValueExpression: string
                      description: string
                      fields:
                        - categories:
                            names:
                              - type: string
                          collation: string
                          dataPolicies:
                            - name: string
                          defaultValueExpression: string
                          description: string
                          fields:
                            - categories:
                                names:
                                  - {}
                              collation: string
                              dataPolicies:
                                - name: string
                              defaultValueExpression: string
                              description: string
                              fields:
                                - categories: {}
                                  collation: string
                                  dataPolicies:
                                    - {}
                                  defaultValueExpression: string
                                  description: string
                                  fields:
                                    - {}
                                  foreignTypeDefinition: string
                                  maxLength: string
                                  mode: string
                                  name: string
                                  policyTags: {}
                                  precision: string
                                  rangeElementType: {}
                                  roundingMode: string
                                  scale: string
                                  type: string
                              foreignTypeDefinition: string
                              maxLength: string
                              mode: string
                              name: string
                              policyTags:
                                names:
                                  - {}
                              precision: string
                              rangeElementType:
                                type: string
                              roundingMode: string
                              scale: string
                              type: string
                          foreignTypeDefinition: string
                          maxLength: string
                          mode: string
                          name: string
                          policyTags:
                            names:
                              - type: string
                          precision: string
                          rangeElementType:
                            type: string
                          roundingMode: string
                          scale: string
                          type: string
                      foreignTypeDefinition: string
                      maxLength: string
                      mode: string
                      name: string
                      policyTags:
                        names:
                          - type: string
                      precision: string
                      rangeElementType:
                        type: string
                      roundingMode: string
                      scale: string
                      type: string
                  foreignTypeDefinition: string
                  maxLength: string
                  mode: string
                  name: string
                  policyTags:
                    names:
                      - type: string
                  precision: string
                  rangeElementType:
                    type: string
                  roundingMode: string
                  scale: string
                  type: string
              foreignTypeDefinition: string
              maxLength: string
              mode: string
              name: string
              policyTags:
                names:
                  - type: string
              precision: string
              rangeElementType:
                type: string
              roundingMode: string
              scale: string
              type: string
          foreignTypeDefinition: string
          maxLength: string
          mode: string
          name: string
          policyTags:
            names:
              - type: string
          precision: string
          rangeElementType:
            type: string
          roundingMode: string
          scale: string
          type: string
      foreignTypeInfo:
        typeSystem: string
    schemaInline: string
    schemaInlineFormat: string
    schemaUpdateOptions:
      - type: string
    skipLeadingRows: integer
    sourceFormat: string
    sourceUris:
      - type: string
    timePartitioning:
      expirationMs: string
      field: string
      requirePartitionFilter: boolean
      type: string
    useAvroLogicalTypes: boolean
    writeDisposition: string
  query:
    allowLargeResults: boolean
    connectionProperties:
      - key: string
        value: string
    continuous: boolean
    createDisposition: string
    createSession: boolean
    defaultDataset:
      datasetId: string
      projectId: string
    flattenResults: boolean
    maximumBillingTier: integer
    maximumBytesBilled: string
    parameterMode: string
    preserveNulls: boolean
    priority: string
    query: string
    queryParameters:
      - name: string
        parameterType:
          structTypes:
            - description: string
              name: string
          type: string
        parameterValue:
          arrayValues:
            - arrayValues:
                - arrayValues:
                    - arrayValues:
                        - arrayValues:
                            - arrayValues:
                                - arrayValues:
                                    - {}
                                  rangeValue: {}
                                  structValues: object
                                  value: string
                              structValues: object
                              value: string
                          structValues: object
                          value: string
                      structValues: object
                      value: string
                  structValues: object
                  value: string
              structValues: object
              value: string
          structValues: object
          value: string
    schemaUpdateOptions:
      - type: string
    scriptOptions:
      keyResultStatement: string
      statementByteBudget: string
      statementTimeoutMs: string
    systemVariables:
      types: object
      values: object
    tableDefinitions: object
    useLegacySql: boolean
    useQueryCache: boolean
    userDefinedFunctionResources:
      - inlineCode: string
        resourceUri: string
    writeDisposition: string
etag: string
id: string
jobCreationReason:
  code: string
jobReference:
  jobId: string
  location: string
  projectId: string
kind: string
principal_subject: string
selfLink: string
statistics:
  completionRatio: number
  copy:
    copiedLogicalBytes: string
    copiedRows: string
  creationTime: string
  dataMaskingStatistics:
    dataMaskingApplied: boolean
  edition: string
  endTime: string
  extract:
    destinationUriFileCounts:
      - format: string
        type: string
    inputBytes: string
    timeline:
      - activeUnits: string
        completedUnits: string
        elapsedMs: string
        estimatedRunnableUnits: string
        pendingUnits: string
        totalSlotMs: string
  finalExecutionDurationMs: string
  load:
    badRecords: string
    inputFileBytes: string
    inputFiles: string
    outputBytes: string
    outputRows: string
    timeline:
      - activeUnits: string
        completedUnits: string
        elapsedMs: string
        estimatedRunnableUnits: string
        pendingUnits: string
        totalSlotMs: string
  numChildJobs: string
  parentJobId: string
  query:
    biEngineStatistics:
      accelerationMode: string
      biEngineMode: string
      biEngineReasons:
        - code: string
          message: string
    billingTier: integer
    cacheHit: boolean
    ddlAffectedRowAccessPolicyCount: string
    ddlOperationPerformed: string
    ddlTargetRoutine:
      datasetId: string
      projectId: string
      routineId: string
    ddlTargetRowAccessPolicy:
      datasetId: string
      policyId: string
      projectId: string
      tableId: string
    dmlStats:
      deletedRowCount: string
      insertedRowCount: string
      updatedRowCount: string
    estimatedBytesProcessed: string
    exportDataStatistics:
      fileCount: string
      rowCount: string
    externalServiceCosts:
      - bytesBilled: string
        bytesProcessed: string
        externalService: string
        reservedSlotCount: string
        slotMs: string
    loadQueryStatistics:
      badRecords: string
      bytesTransferred: string
      inputFileBytes: string
      inputFiles: string
      outputBytes: string
      outputRows: string
    materializedViewStatistics:
      materializedView:
        - chosen: boolean
          estimatedBytesSaved: string
          rejectedReason: string
    metadataCacheStatistics:
      tableMetadataCacheUsage:
        - explanation: string
          staleness: string
          tableType: string
          unusedReason: string
    mlStatistics:
      hparamTrials:
        - endTimeMs: string
          errorMessage: string
          evalLoss: number
          evaluationMetrics:
            arimaForecastingMetrics:
              arimaFittingMetrics:
                - aic: number
                  logLikelihood: number
                  variance: number
              arimaSingleModelForecastingMetrics:
                - arimaFittingMetrics:
                    aic: number
                    logLikelihood: number
                    variance: number
                  hasDrift: boolean
                  hasHolidayEffect: boolean
                  hasSpikesAndDips: boolean
                  hasStepChanges: boolean
                  nonSeasonalOrder:
                    d: string
                    p: string
                    q: string
                  seasonalPeriods:
                    - enum: string
                      enumDescriptions: string
                      type: string
                  timeSeriesId: string
                  timeSeriesIds:
                    - type: string
              hasDrift:
                - type: string
              nonSeasonalOrder:
                - d: string
                  p: string
                  q: string
              seasonalPeriods:
                - enum: string
                  enumDescriptions: string
                  type: string
              timeSeriesId:
                - type: string
            binaryClassificationMetrics:
              aggregateClassificationMetrics:
                accuracy: number
                f1Score: number
                logLoss: number
                precision: number
                recall: number
                rocAuc: number
                threshold: number
              binaryConfusionMatrixList:
                - accuracy: number
                  f1Score: number
                  falseNegatives: string
                  falsePositives: string
                  positiveClassThreshold: number
                  precision: number
                  recall: number
                  trueNegatives: string
                  truePositives: string
              negativeLabel: string
              positiveLabel: string
            clusteringMetrics:
              clusters:
                - centroidId: string
                  count: string
                  featureValues:
                    - categoricalValue:
                        categoryCounts:
                          - category: string
                            count: string
                      featureColumn: string
                      numericalValue: number
              daviesBouldinIndex: number
              meanSquaredDistance: number
            dimensionalityReductionMetrics:
              totalExplainedVarianceRatio: number
            multiClassClassificationMetrics:
              confusionMatrixList:
                - confidenceThreshold: number
                  rows:
                    - actualLabel: string
                      entries:
                        - itemCount: string
                          predictedLabel: string
            rankingMetrics:
              averageRank: number
              meanAveragePrecision: number
              meanSquaredError: number
              normalizedDiscountedCumulativeGain: number
            regressionMetrics:
              meanAbsoluteError: number
              meanSquaredError: number
              meanSquaredLogError: number
              medianAbsoluteError: number
              rSquared: number
          hparams:
            activationFn: string
            adjustStepChanges: boolean
            approxGlobalFeatureContrib: boolean
            autoArima: boolean
            autoArimaMaxOrder: string
            autoArimaMinOrder: string
            autoClassWeights: boolean
            batchSize: string
            boosterType: string
            budgetHours: number
            calculatePValues: boolean
            categoryEncodingMethod: string
            cleanSpikesAndDips: boolean
            colorSpace: string
            colsampleBylevel: number
            colsampleBynode: number
            colsampleBytree: number
            dartNormalizeType: string
            dataFrequency: string
            dataSplitColumn: string
            dataSplitEvalFraction: number
            dataSplitMethod: string
            decomposeTimeSeries: boolean
            distanceType: string
            dropout: number
            earlyStop: boolean
            enableGlobalExplain: boolean
            feedbackType: string
            fitIntercept: boolean
            hiddenUnits:
              - format: string
                type: string
            holidayRegion: string
            holidayRegions:
              - enum: string
                enumDescriptions: string
                type: string
            horizon: string
            hparamTuningObjectives:
              - enum: string
                enumDescriptions: string
                type: string
            includeDrift: boolean
            initialLearnRate: number
            inputLabelColumns:
              - type: string
            instanceWeightColumn: string
            integratedGradientsNumSteps: string
            itemColumn: string
            kmeansInitializationColumn: string
            kmeansInitializationMethod: string
            l1RegActivation: number
            l1Regularization: number
            l2Regularization: number
            labelClassWeights: object
            learnRate: number
            learnRateStrategy: string
            lossType: string
            maxIterations: string
            maxParallelTrials: string
            maxTimeSeriesLength: string
            maxTreeDepth: string
            minRelativeProgress: number
            minSplitLoss: number
            minTimeSeriesLength: string
            minTreeChildWeight: string
            modelRegistry: string
            modelUri: string
            numClusters: string
            numFactors: string
            numParallelTree: string
            numPrincipalComponents: string
            numTrials: string
            optimizationStrategy: string
            optimizer: string
            pcaExplainedVarianceRatio: number
            pcaSolver: string
            sampledShapleyNumPaths: string
            scaleFeatures: boolean
            standardizeFeatures: boolean
            subsample: number
            tfVersion: string
            timeSeriesDataColumn: string
            timeSeriesIdColumn: string
            timeSeriesIdColumns:
              - type: string
            timeSeriesLengthFraction: number
            timeSeriesTimestampColumn: string
            treeMethod: string
            trendSmoothingWindowSize: string
            userColumn: string
            vertexAiModelVersionAliases:
              - type: string
            walsAlpha: number
            warmStart: boolean
            xgboostVersion: string
          startTimeMs: string
          status: string
          trainingLoss: number
          trialId: string
      iterationResults:
        - arimaResult:
            arimaModelInfo:
              - arimaCoefficients:
                  autoRegressiveCoefficients:
                    - format: string
                      type: string
                  interceptCoefficient: number
                  movingAverageCoefficients:
                    - format: string
                      type: string
                hasDrift: boolean
                hasHolidayEffect: boolean
                hasSpikesAndDips: boolean
                hasStepChanges: boolean
                seasonalPeriods:
                  - enum: string
                    enumDescriptions: string
                    type: string
                timeSeriesId: string
                timeSeriesIds:
                  - type: string
            seasonalPeriods:
              - enum: string
                enumDescriptions: string
                type: string
          clusterInfos:
            - centroidId: string
              clusterRadius: number
              clusterSize: string
          durationMs: string
          evalLoss: number
          index: integer
          learnRate: number
          principalComponentInfos:
            - cumulativeExplainedVarianceRatio: number
              explainedVariance: number
              explainedVarianceRatio: number
              principalComponentId: string
          trainingLoss: number
      maxIterations: string
      modelType: string
      trainingType: string
    modelTraining:
      currentIteration: integer
      expectedTotalIterations: string
    modelTrainingCurrentIteration: integer
    modelTrainingExpectedTotalIteration: string
    numDmlAffectedRows: string
    performanceInsights:
      avgPreviousExecutionMs: string
      stagePerformanceChangeInsights:
        - inputDataChange:
            recordsReadDiffPercentage: number
          stageId: string
      stagePerformanceStandaloneInsights:
        - biEngineReasons:
            - code: string
              message: string
          highCardinalityJoins:
            - leftRows: string
              outputRows: string
              rightRows: string
              stepIndex: integer
          insufficientShuffleQuota: boolean
          partitionSkew:
            skewSources:
              - stageId: string
          slotContention: boolean
          stageId: string
    queryInfo:
      optimizationDetails: object
    queryPlan:
      - completedParallelInputs: string
        computeMode: string
        computeMsAvg: string
        computeMsMax: string
        computeRatioAvg: number
        computeRatioMax: number
        endMs: string
        id: string
        inputStages:
          - format: string
            type: string
        name: string
        parallelInputs: string
        readMsAvg: string
        readMsMax: string
        readRatioAvg: number
        readRatioMax: number
        recordsRead: string
        recordsWritten: string
        shuffleOutputBytes: string
        shuffleOutputBytesSpilled: string
        slotMs: string
        startMs: string
        status: string
        steps:
          - kind: string
            substeps:
              - type: string
        waitMsAvg: string
        waitMsMax: string
        waitRatioAvg: number
        waitRatioMax: number
        writeMsAvg: string
        writeMsMax: string
        writeRatioAvg: number
        writeRatioMax: number
    referencedRoutines:
      - datasetId: string
        projectId: string
        routineId: string
    referencedTables:
      - datasetId: string
        projectId: string
        tableId: string
    reservationUsage:
      - name: string
        slotMs: string
    searchStatistics:
      indexUnusedReasons:
        - code: string
          indexName: string
          message: string
      indexUsageMode: string
    sparkStatistics:
      endpoints: object
      gcsStagingBucket: string
      kmsKeyName: string
      loggingInfo:
        projectId: string
        resourceType: string
      sparkJobId: string
      sparkJobLocation: string
    statementType: string
    timeline:
      - activeUnits: string
        completedUnits: string
        elapsedMs: string
        estimatedRunnableUnits: string
        pendingUnits: string
        totalSlotMs: string
    totalBytesBilled: string
    totalBytesProcessed: string
    totalBytesProcessedAccuracy: string
    totalPartitionsProcessed: string
    totalSlotMs: string
    transferredBytes: string
    undeclaredQueryParameters:
      - name: string
    vectorSearchStatistics:
      indexUnusedReasons:
        - code: string
          indexName: string
          message: string
      indexUsageMode: string
  quotaDeferments:
    - type: string
  reservationUsage:
    - name: string
      slotMs: string
  reservation_id: string
  rowLevelSecurityStatistics:
    rowLevelSecurityApplied: boolean
  scriptStatistics:
    evaluationKind: string
    stackFrames:
      - endColumn: integer
        endLine: integer
        procedureId: string
        startColumn: integer
        startLine: integer
        text: string
  sessionInfo:
    sessionId: string
  startTime: string
  totalBytesProcessed: string
  totalSlotMs: string
  transactionInfo:
    transactionId: string
status:
  errorResult:
    debugInfo: string
    location: string
    message: string
    reason: string
  errors:
    - debugInfo: string
      location: string
      message: string
      reason: string
  state: string
user_email: string

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
