---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - transcoder
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.transcoder.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the job. Format: `projects/{project_number}/locations/{location}/jobs/{job}` |
| <CopyableCode code="batchModePriority" /> | `integer` | The processing priority of a batch job. This field can only be set for batch mode jobs. The default value is 0. This value cannot be negative. Higher values correspond to higher priorities for the job. |
| <CopyableCode code="config" /> | `object` | Job configuration |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the job was created. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time the transcoding finished. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="inputUri" /> | `string` | Input only. Specify the `input_uri` to populate empty `uri` fields in each element of `Job.config.inputs` or `JobTemplate.config.inputs` when using template. URI of the media. Input files must be at least 5 seconds in duration and stored in Cloud Storage (for example, `gs://bucket/inputs/file.mp4`). See [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats). |
| <CopyableCode code="labels" /> | `object` | The labels associated with this job. You can use these to organize and group your jobs. |
| <CopyableCode code="mode" /> | `string` | The processing mode of the job. The default is `PROCESSING_MODE_INTERACTIVE`. |
| <CopyableCode code="optimization" /> | `string` | Optional. The optimization strategy of the job. The default is `AUTODETECT`. |
| <CopyableCode code="outputUri" /> | `string` | Input only. Specify the `output_uri` to populate an empty `Job.config.output.uri` or `JobTemplate.config.output.uri` when using template. URI for the output file(s). For example, `gs://my-bucket/outputs/`. See [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats). |
| <CopyableCode code="startTime" /> | `string` | Output only. The time the transcoding started. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the job. |
| <CopyableCode code="templateId" /> | `string` | Input only. Specify the `template_id` to use for populating `Job.config`. The default is `preset/web-hd`, which is the only supported preset. User defined JobTemplate: `{job_template_id}` |
| <CopyableCode code="ttlAfterCompletionDays" /> | `integer` | Job time to live value in days, which will be effective after job completion. Job should be deleted automatically after the given TTL. Enter a value between 1 and 90. The default is 30. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Returns the job data. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists jobs in the specified region. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a job in the specified region. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Deletes a job. |

## `SELECT` examples

Lists jobs in the specified region.

```sql
SELECT
name,
batchModePriority,
config,
createTime,
endTime,
error,
inputUri,
labels,
mode,
optimization,
outputUri,
startTime,
state,
templateId,
ttlAfterCompletionDays
FROM google.transcoder.jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
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
INSERT INTO google.transcoder.jobs (
locationsId,
projectsId,
name,
inputUri,
outputUri,
templateId,
config,
ttlAfterCompletionDays,
labels,
mode,
batchModePriority,
optimization
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ inputUri }}',
'{{ outputUri }}',
'{{ templateId }}',
'{{ config }}',
'{{ ttlAfterCompletionDays }}',
'{{ labels }}',
'{{ mode }}',
'{{ batchModePriority }}',
'{{ optimization }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: inputUri
      value: string
    - name: outputUri
      value: string
    - name: templateId
      value: string
    - name: config
      value:
        - name: inputs
          value:
            - - name: key
                value: string
              - name: uri
                value: string
              - name: preprocessingConfig
                value:
                  - name: color
                    value:
                      - name: saturation
                        value: number
                      - name: contrast
                        value: number
                      - name: brightness
                        value: number
                  - name: denoise
                    value:
                      - name: strength
                        value: number
                      - name: tune
                        value: string
                  - name: deblock
                    value:
                      - name: strength
                        value: number
                      - name: enabled
                        value: boolean
                  - name: audio
                    value:
                      - name: lufs
                        value: number
                      - name: highBoost
                        value: boolean
                      - name: lowBoost
                        value: boolean
                  - name: crop
                    value:
                      - name: topPixels
                        value: integer
                      - name: bottomPixels
                        value: integer
                      - name: leftPixels
                        value: integer
                      - name: rightPixels
                        value: integer
                  - name: pad
                    value:
                      - name: topPixels
                        value: integer
                      - name: bottomPixels
                        value: integer
                      - name: leftPixels
                        value: integer
                      - name: rightPixels
                        value: integer
                  - name: deinterlace
                    value:
                      - name: yadif
                        value:
                          - name: mode
                            value: string
                          - name: disableSpatialInterlacing
                            value: boolean
                          - name: parity
                            value: string
                          - name: deinterlaceAllFrames
                            value: boolean
                      - name: bwdif
                        value:
                          - name: mode
                            value: string
                          - name: parity
                            value: string
                          - name: deinterlaceAllFrames
                            value: boolean
        - name: editList
          value:
            - - name: key
                value: string
              - name: inputs
                value:
                  - string
              - name: endTimeOffset
                value: string
              - name: startTimeOffset
                value: string
        - name: elementaryStreams
          value:
            - - name: key
                value: string
              - name: videoStream
                value:
                  - name: h264
                    value:
                      - name: widthPixels
                        value: integer
                      - name: heightPixels
                        value: integer
                      - name: frameRate
                        value: number
                      - name: frameRateConversionStrategy
                        value: string
                      - name: bitrateBps
                        value: integer
                      - name: pixelFormat
                        value: string
                      - name: rateControlMode
                        value: string
                      - name: crfLevel
                        value: integer
                      - name: allowOpenGop
                        value: boolean
                      - name: gopFrameCount
                        value: integer
                      - name: gopDuration
                        value: string
                      - name: enableTwoPass
                        value: boolean
                      - name: vbvSizeBits
                        value: integer
                      - name: vbvFullnessBits
                        value: integer
                      - name: entropyCoder
                        value: string
                      - name: bPyramid
                        value: boolean
                      - name: bFrameCount
                        value: integer
                      - name: aqStrength
                        value: number
                      - name: profile
                        value: string
                      - name: tune
                        value: string
                      - name: preset
                        value: string
                      - name: sdr
                        value: []
                      - name: hlg
                        value: []
                  - name: h265
                    value:
                      - name: widthPixels
                        value: integer
                      - name: heightPixels
                        value: integer
                      - name: frameRate
                        value: number
                      - name: frameRateConversionStrategy
                        value: string
                      - name: bitrateBps
                        value: integer
                      - name: pixelFormat
                        value: string
                      - name: rateControlMode
                        value: string
                      - name: crfLevel
                        value: integer
                      - name: allowOpenGop
                        value: boolean
                      - name: gopFrameCount
                        value: integer
                      - name: gopDuration
                        value: string
                      - name: enableTwoPass
                        value: boolean
                      - name: vbvSizeBits
                        value: integer
                      - name: vbvFullnessBits
                        value: integer
                      - name: bPyramid
                        value: boolean
                      - name: bFrameCount
                        value: integer
                      - name: aqStrength
                        value: number
                      - name: profile
                        value: string
                      - name: tune
                        value: string
                      - name: preset
                        value: string
                      - name: sdr
                        value: []
                      - name: hlg
                        value: []
                      - name: hdr10
                        value: []
                  - name: vp9
                    value:
                      - name: widthPixels
                        value: integer
                      - name: heightPixels
                        value: integer
                      - name: frameRate
                        value: number
                      - name: frameRateConversionStrategy
                        value: string
                      - name: bitrateBps
                        value: integer
                      - name: pixelFormat
                        value: string
                      - name: rateControlMode
                        value: string
                      - name: crfLevel
                        value: integer
                      - name: gopFrameCount
                        value: integer
                      - name: gopDuration
                        value: string
                      - name: profile
                        value: string
                      - name: sdr
                        value: []
                      - name: hlg
                        value: []
              - name: audioStream
                value:
                  - name: codec
                    value: string
                  - name: bitrateBps
                    value: integer
                  - name: channelCount
                    value: integer
                  - name: channelLayout
                    value:
                      - string
                  - name: mapping
                    value:
                      - - name: atomKey
                          value: string
                        - name: inputKey
                          value: string
                        - name: inputTrack
                          value: integer
                        - name: inputChannel
                          value: integer
                        - name: outputChannel
                          value: integer
                        - name: gainDb
                          value: number
                  - name: sampleRateHertz
                    value: integer
                  - name: languageCode
                    value: string
                  - name: displayName
                    value: string
              - name: textStream
                value:
                  - name: codec
                    value: string
                  - name: languageCode
                    value: string
                  - name: mapping
                    value:
                      - - name: atomKey
                          value: string
                        - name: inputKey
                          value: string
                        - name: inputTrack
                          value: integer
                  - name: displayName
                    value: string
        - name: muxStreams
          value:
            - - name: key
                value: string
              - name: fileName
                value: string
              - name: container
                value: string
              - name: elementaryStreams
                value:
                  - string
              - name: segmentSettings
                value:
                  - name: segmentDuration
                    value: string
                  - name: individualSegments
                    value: boolean
              - name: encryptionId
                value: string
              - name: fmp4
                value:
                  - name: codecTag
                    value: string
        - name: manifests
          value:
            - - name: fileName
                value: string
              - name: type
                value: string
              - name: muxStreams
                value:
                  - string
              - name: dash
                value:
                  - name: segmentReferenceScheme
                    value: string
        - name: output
          value:
            - name: uri
              value: string
        - name: adBreaks
          value:
            - - name: startTimeOffset
                value: string
        - name: pubsubDestination
          value:
            - name: topic
              value: string
        - name: spriteSheets
          value:
            - - name: format
                value: string
              - name: filePrefix
                value: string
              - name: spriteWidthPixels
                value: integer
              - name: spriteHeightPixels
                value: integer
              - name: columnCount
                value: integer
              - name: rowCount
                value: integer
              - name: startTimeOffset
                value: string
              - name: endTimeOffset
                value: string
              - name: totalCount
                value: integer
              - name: interval
                value: string
              - name: quality
                value: integer
        - name: overlays
          value:
            - - name: image
                value:
                  - name: uri
                    value: string
                  - name: resolution
                    value:
                      - name: x
                        value: number
                      - name: 'y'
                        value: number
                  - name: alpha
                    value: number
              - name: animations
                value:
                  - - name: animationStatic
                      value:
                        - name: startTimeOffset
                          value: string
                    - name: animationFade
                      value:
                        - name: fadeType
                          value: string
                        - name: startTimeOffset
                          value: string
                        - name: endTimeOffset
                          value: string
                    - name: animationEnd
                      value:
                        - name: startTimeOffset
                          value: string
        - name: encryptions
          value:
            - - name: id
                value: string
              - name: aes128
                value: []
              - name: sampleAes
                value: []
              - name: mpegCenc
                value:
                  - name: scheme
                    value: string
              - name: secretManagerKeySource
                value:
                  - name: secretVersion
                    value: string
              - name: drmSystems
                value:
                  - name: widevine
                    value: []
                  - name: fairplay
                    value: []
                  - name: playready
                    value: []
                  - name: clearkey
                    value: []
    - name: state
      value: string
    - name: createTime
      value: string
    - name: startTime
      value: string
    - name: endTime
      value: string
    - name: ttlAfterCompletionDays
      value: integer
    - name: labels
      value: object
    - name: error
      value:
        - name: code
          value: integer
        - name: message
          value: string
        - name: details
          value:
            - object
    - name: mode
      value: string
    - name: batchModePriority
      value: integer
    - name: optimization
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.transcoder.jobs
WHERE jobsId = '{{ jobsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
