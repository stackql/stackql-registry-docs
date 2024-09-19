---
title: job_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - job_templates
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

Creates, updates, deletes, gets or lists a <code>job_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.transcoder.job_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the job template. Format: `projects/{project_number}/locations/{location}/jobTemplates/{job_template}` |
| <CopyableCode code="config" /> | `object` | Job configuration |
| <CopyableCode code="labels" /> | `object` | The labels associated with this job template. You can use these to organize and group your job templates. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobTemplatesId, locationsId, projectsId" /> | Returns the job template data. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists job templates in the specified region. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a job template in the specified region. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobTemplatesId, locationsId, projectsId" /> | Deletes a job template. |

## `SELECT` examples

Lists job templates in the specified region.

```sql
SELECT
name,
config,
labels
FROM google.transcoder.job_templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_templates</code> resource.

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
INSERT INTO google.transcoder.job_templates (
locationsId,
projectsId,
name,
config,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ config }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
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
    - name: labels
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>job_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.transcoder.job_templates
WHERE jobTemplatesId = '{{ jobTemplatesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
