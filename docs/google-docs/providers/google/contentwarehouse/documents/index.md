---
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
  - contentwarehouse
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

Creates, updates, deletes, gets or lists a <code>documents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contentwarehouse.documents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the document. Format: projects/{project_number}/locations/{location}/documents/{document_id}. The name is ignored when creating a document. |
| <CopyableCode code="cloudAiDocument" /> | `object` | Document represents the canonical document resource in Document AI. It is an interchange format that provides insights into documents and allows for collaboration between users and Document AI to iterate and optimize for quality. |
| <CopyableCode code="contentCategory" /> | `string` | Indicates the category (image, audio, video etc.) of the original content. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the document is created. |
| <CopyableCode code="creator" /> | `string` | The user who creates the document. |
| <CopyableCode code="displayName" /> | `string` | Required. Display name of the document given by the user. This name will be displayed in the UI. Customer can populate this field with the name of the document. This differs from the 'title' field as 'title' is optional and stores the top heading in the document. |
| <CopyableCode code="displayUri" /> | `string` | Uri to display the document, for example, in the UI. |
| <CopyableCode code="dispositionTime" /> | `string` | Output only. If linked to a Collection with RetentionPolicy, the date when the document becomes mutable. |
| <CopyableCode code="documentSchemaName" /> | `string` | The Document schema name. Format: projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}. |
| <CopyableCode code="inlineRawDocument" /> | `string` | Raw document content. |
| <CopyableCode code="legalHold" /> | `boolean` | Output only. Indicates if the document has a legal hold on it. |
| <CopyableCode code="plainText" /> | `string` | Other document format, such as PPTX, XLXS |
| <CopyableCode code="properties" /> | `array` | List of values that are user supplied metadata. |
| <CopyableCode code="rawDocumentFileType" /> | `string` | This is used when DocAI was not used to load the document and parsing/ extracting is needed for the inline_raw_document. For example, if inline_raw_document is the byte representation of a PDF file, then this should be set to: RAW_DOCUMENT_FILE_TYPE_PDF. |
| <CopyableCode code="rawDocumentPath" /> | `string` | Raw document file in Cloud Storage path. |
| <CopyableCode code="referenceId" /> | `string` | The reference ID set by customers. Must be unique per project and location. |
| <CopyableCode code="textExtractionDisabled" /> | `boolean` | If true, text extraction will not be performed. |
| <CopyableCode code="textExtractionEnabled" /> | `boolean` | If true, text extraction will be performed. |
| <CopyableCode code="title" /> | `string` | Title that describes the document. This can be the top heading or text that describes the document. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the document is last updated. |
| <CopyableCode code="updater" /> | `string` | The user who lastly updates the document. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Gets a document. Returns NOT_FOUND if the document does not exist. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a document. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Deletes a document. Returns NOT_FOUND if the document does not exist. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name. |
| <CopyableCode code="linked_sources" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Return all source document-links from the document. |
| <CopyableCode code="linked_targets" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Return all target document-links from the document. |
| <CopyableCode code="lock" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Lock the document so the document cannot be updated by other users. |
| <CopyableCode code="search" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against. |
| <CopyableCode code="set_acl" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Sets the access control policy for a resource. Replaces any existing policy. |

## `SELECT` examples

Gets a document. Returns NOT_FOUND if the document does not exist.

```sql
SELECT
name,
cloudAiDocument,
contentCategory,
createTime,
creator,
displayName,
displayUri,
dispositionTime,
documentSchemaName,
inlineRawDocument,
legalHold,
plainText,
properties,
rawDocumentFileType,
rawDocumentPath,
referenceId,
textExtractionDisabled,
textExtractionEnabled,
title,
updateTime,
updater
FROM google.contentwarehouse.documents
WHERE documentsId = '{{ documentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>documents</code> resource.

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
INSERT INTO google.contentwarehouse.documents (
locationsId,
projectsId,
cloudAiDocumentOption,
requestMetadata,
policy,
createMask,
document
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ cloudAiDocumentOption }}',
'{{ requestMetadata }}',
'{{ policy }}',
'{{ createMask }}',
'{{ document }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: cloudAiDocumentOption
      value:
        - name: customizedEntitiesPropertiesConversions
          value: object
        - name: enableEntitiesConversions
          value: boolean
    - name: requestMetadata
      value:
        - name: userInfo
          value:
            - name: groupIds
              value:
                - string
            - name: id
              value: string
    - name: policy
      value:
        - name: etag
          value: string
        - name: bindings
          value:
            - - name: members
                value:
                  - string
              - name: role
                value: string
              - name: condition
                value:
                  - name: location
                    value: string
                  - name: expression
                    value: string
                  - name: title
                    value: string
                  - name: description
                    value: string
        - name: auditConfigs
          value:
            - - name: service
                value: string
              - name: auditLogConfigs
                value:
                  - - name: exemptedMembers
                      value:
                        - string
                    - name: logType
                      value: string
        - name: version
          value: integer
    - name: createMask
      value: string
    - name: document
      value:
        - name: referenceId
          value: string
        - name: title
          value: string
        - name: updater
          value: string
        - name: creator
          value: string
        - name: rawDocumentFileType
          value: string
        - name: inlineRawDocument
          value: string
        - name: legalHold
          value: boolean
        - name: createTime
          value: string
        - name: contentCategory
          value: string
        - name: cloudAiDocument
          value:
            - name: revisions
              value:
                - - name: parent
                    value:
                      - integer
                  - name: humanReview
                    value:
                      - name: state
                        value: string
                      - name: stateMessage
                        value: string
                  - name: id
                    value: string
                  - name: createTime
                    value: string
                  - name: processor
                    value: string
                  - name: parentIds
                    value:
                      - string
                  - name: agent
                    value: string
            - name: pages
              value:
                - - name: imageQualityScores
                    value:
                      - name: detectedDefects
                        value:
                          - - name: type
                              value: string
                            - name: confidence
                              value: number
                      - name: qualityScore
                        value: number
                  - name: tables
                    value:
                      - - name: layout
                          value:
                            - name: boundingPoly
                              value:
                                - name: normalizedVertices
                                  value:
                                    - - name: 'y'
                                        value: number
                                      - name: x
                                        value: number
                                - name: vertices
                                  value:
                                    - - name: 'y'
                                        value: integer
                                      - name: x
                                        value: integer
                            - name: orientation
                              value: string
                            - name: textAnchor
                              value:
                                - name: textSegments
                                  value:
                                    - - name: startIndex
                                        value: string
                                      - name: endIndex
                                        value: string
                                - name: content
                                  value: string
                            - name: confidence
                              value: number
                        - name: detectedLanguages
                          value:
                            - - name: languageCode
                                value: string
                              - name: confidence
                                value: number
                        - name: headerRows
                          value:
                            - - name: cells
                                value:
                                  - - name: colSpan
                                      value: integer
                                    - name: detectedLanguages
                                      value:
                                        - - name: languageCode
                                            value: string
                                          - name: confidence
                                            value: number
                                    - name: rowSpan
                                      value: integer
                        - name: bodyRows
                          value:
                            - - name: cells
                                value:
                                  - - name: colSpan
                                      value: integer
                                    - name: detectedLanguages
                                      value:
                                        - - name: languageCode
                                            value: string
                                          - name: confidence
                                            value: number
                                    - name: rowSpan
                                      value: integer
                        - name: provenance
                          value:
                            - name: id
                              value: integer
                            - name: revision
                              value: integer
                            - name: parents
                              value:
                                - - name: revision
                                    value: integer
                                  - name: id
                                    value: integer
                                  - name: index
                                    value: integer
                            - name: type
                              value: string
                  - name: image
                    value:
                      - name: content
                        value: string
                      - name: width
                        value: integer
                      - name: mimeType
                        value: string
                      - name: height
                        value: integer
                  - name: formFields
                    value:
                      - - name: correctedKeyText
                          value: string
                        - name: valueDetectedLanguages
                          value:
                            - - name: languageCode
                                value: string
                              - name: confidence
                                value: number
                        - name: valueType
                          value: string
                        - name: nameDetectedLanguages
                          value:
                            - - name: languageCode
                                value: string
                              - name: confidence
                                value: number
                        - name: correctedValueText
                          value: string
                  - name: pageNumber
                    value: integer
                  - name: detectedBarcodes
                    value:
                      - - name: barcode
                          value:
                            - name: rawValue
                              value: string
                            - name: format
                              value: string
                            - name: valueFormat
                              value: string
                  - name: tokens
                    value:
                      - - name: detectedLanguages
                          value:
                            - - name: languageCode
                                value: string
                              - name: confidence
                                value: number
                        - name: detectedBreak
                          value:
                            - name: type
                              value: string
                        - name: styleInfo
                          value:
                            - name: textColor
                              value:
                                - name: green
                                  value: number
                                - name: red
                                  value: number
                                - name: alpha
                                  value: number
                                - name: blue
                                  value: number
                            - name: strikeout
                              value: boolean
                            - name: fontSize
                              value: integer
                            - name: underlined
                              value: boolean
                            - name: handwritten
                              value: boolean
                            - name: letterSpacing
                              value: number
                            - name: bold
                              value: boolean
                            - name: fontType
                              value: string
                            - name: fontWeight
                              value: integer
                            - name: smallcaps
                              value: boolean
                            - name: subscript
                              value: boolean
                            - name: pixelFontSize
                              value: number
                            - name: italic
                              value: boolean
                            - name: superscript
                              value: boolean
                  - name: detectedLanguages
                    value:
                      - - name: languageCode
                          value: string
                        - name: confidence
                          value: number
                  - name: symbols
                    value:
                      - - name: detectedLanguages
                          value:
                            - - name: languageCode
                                value: string
                              - name: confidence
                                value: number
                  - name: lines
                    value:
                      - - name: detectedLanguages
                          value:
                            - - name: languageCode
                                value: string
                              - name: confidence
                                value: number
                  - name: transforms
                    value:
                      - - name: type
                          value: integer
                        - name: data
                          value: string
                        - name: rows
                          value: integer
                        - name: cols
                          value: integer
                  - name: visualElements
                    value:
                      - - name: detectedLanguages
                          value:
                            - - name: languageCode
                                value: string
                              - name: confidence
                                value: number
                        - name: type
                          value: string
                  - name: paragraphs
                    value:
                      - - name: detectedLanguages
                          value:
                            - - name: languageCode
                                value: string
                              - name: confidence
                                value: number
                  - name: dimension
                    value:
                      - name: unit
                        value: string
                      - name: height
                        value: number
                      - name: width
                        value: number
                  - name: blocks
                    value:
                      - - name: detectedLanguages
                          value:
                            - - name: languageCode
                                value: string
                              - name: confidence
                                value: number
            - name: entityRelations
              value:
                - - name: objectId
                    value: string
                  - name: relation
                    value: string
                  - name: subjectId
                    value: string
            - name: content
              value: string
            - name: shardInfo
              value:
                - name: shardIndex
                  value: string
                - name: shardCount
                  value: string
                - name: textOffset
                  value: string
            - name: chunkedDocument
              value:
                - name: chunks
                  value:
                    - - name: sourceBlockIds
                        value:
                          - string
                      - name: pageFooters
                        value:
                          - - name: pageSpan
                              value:
                                - name: pageEnd
                                  value: integer
                                - name: pageStart
                                  value: integer
                            - name: text
                              value: string
                      - name: content
                        value: string
                      - name: chunkId
                        value: string
                      - name: pageHeaders
                        value:
                          - - name: text
                              value: string
            - name: entities
              value:
                - - name: type
                    value: string
                  - name: normalizedValue
                    value:
                      - name: datetimeValue
                        value:
                          - name: day
                            value: integer
                          - name: hours
                            value: integer
                          - name: month
                            value: integer
                          - name: timeZone
                            value:
                              - name: version
                                value: string
                              - name: id
                                value: string
                          - name: year
                            value: integer
                          - name: utcOffset
                            value: string
                          - name: minutes
                            value: integer
                          - name: nanos
                            value: integer
                          - name: seconds
                            value: integer
                      - name: text
                        value: string
                      - name: moneyValue
                        value:
                          - name: nanos
                            value: integer
                          - name: currencyCode
                            value: string
                          - name: units
                            value: string
                      - name: booleanValue
                        value: boolean
                      - name: dateValue
                        value:
                          - name: year
                            value: integer
                          - name: day
                            value: integer
                          - name: month
                            value: integer
                      - name: integerValue
                        value: integer
                      - name: floatValue
                        value: number
                      - name: addressValue
                        value:
                          - name: revision
                            value: integer
                          - name: regionCode
                            value: string
                          - name: administrativeArea
                            value: string
                          - name: organization
                            value: string
                          - name: locality
                            value: string
                          - name: sortingCode
                            value: string
                          - name: sublocality
                            value: string
                          - name: addressLines
                            value:
                              - string
                          - name: recipients
                            value:
                              - string
                          - name: languageCode
                            value: string
                          - name: postalCode
                            value: string
                  - name: properties
                    value:
                      - - name: type
                          value: string
                        - name: properties
                          value:
                            - - name: type
                                value: string
                              - name: properties
                                value:
                                  - - name: type
                                      value: string
                                    - name: properties
                                      value:
                                        - - name: type
                                            value: string
                                          - name: properties
                                            value:
                                              - - name: type
                                                  value: string
                                                - name: properties
                                                  value:
                                                    - - name: type
                                                        value: string
                                                      - name: properties
                                                        value:
                                                          - - name: type
                                                              value: string
                                                            - name: properties
                                                              value:
                                                                - []
                                                            - name: id
                                                              value: string
                                                            - name: confidence
                                                              value: number
                                                            - name: redacted
                                                              value: boolean
                                                            - name: mentionText
                                                              value: string
                                                            - name: mentionId
                                                              value: string
                                                            - name: pageAnchor
                                                              value: []
                                                      - name: id
                                                        value: string
                                                      - name: confidence
                                                        value: number
                                                      - name: redacted
                                                        value: boolean
                                                      - name: mentionText
                                                        value: string
                                                      - name: mentionId
                                                        value: string
                                                - name: id
                                                  value: string
                                                - name: confidence
                                                  value: number
                                                - name: redacted
                                                  value: boolean
                                                - name: mentionText
                                                  value: string
                                                - name: mentionId
                                                  value: string
                                          - name: id
                                            value: string
                                          - name: confidence
                                            value: number
                                          - name: redacted
                                            value: boolean
                                          - name: mentionText
                                            value: string
                                          - name: mentionId
                                            value: string
                                    - name: id
                                      value: string
                                    - name: confidence
                                      value: number
                                    - name: redacted
                                      value: boolean
                                    - name: mentionText
                                      value: string
                                    - name: mentionId
                                      value: string
                              - name: id
                                value: string
                              - name: confidence
                                value: number
                              - name: redacted
                                value: boolean
                              - name: mentionText
                                value: string
                              - name: mentionId
                                value: string
                        - name: id
                          value: string
                        - name: confidence
                          value: number
                        - name: redacted
                          value: boolean
                        - name: mentionText
                          value: string
                        - name: mentionId
                          value: string
                  - name: id
                    value: string
                  - name: confidence
                    value: number
                  - name: redacted
                    value: boolean
                  - name: mentionText
                    value: string
                  - name: mentionId
                    value: string
            - name: text
              value: string
            - name: textStyles
              value:
                - - name: fontWeight
                    value: string
                  - name: textStyle
                    value: string
                  - name: fontSize
                    value:
                      - name: unit
                        value: string
                      - name: size
                        value: number
                  - name: textDecoration
                    value: string
                  - name: fontFamily
                    value: string
            - name: mimeType
              value: string
            - name: documentLayout
              value:
                - name: blocks
                  value:
                    - - name: pageSpan
                        value:
                          - name: pageStart
                            value: integer
                          - name: pageEnd
                            value: integer
                      - name: tableBlock
                        value:
                          - name: bodyRows
                            value:
                              - - name: cells
                                  value:
                                    - - name: colSpan
                                        value: integer
                                      - name: rowSpan
                                        value: integer
                                      - name: blocks
                                        value:
                                          - - name: listBlock
                                              value:
                                                - name: listEntries
                                                  value:
                                                    - - name: blocks
                                                        value:
                                                          - []
                                                - name: type
                                                  value: string
                                            - name: blockId
                                              value: string
                                            - name: textBlock
                                              value:
                                                - name: text
                                                  value: string
                                                - name: type
                                                  value: string
                                                - name: blocks
                                                  value:
                                                    - - name: blockId
                                                        value: string
                          - name: headerRows
                            value:
                              - - name: cells
                                  value:
                                    - - name: colSpan
                                        value: integer
                                      - name: rowSpan
                                        value: integer
                                      - name: blocks
                                        value:
                                          - - name: blockId
                                              value: string
                          - name: caption
                            value: string
                      - name: blockId
                        value: string
            - name: uri
              value: string
            - name: textChanges
              value:
                - - name: changedText
                    value: string
                  - name: provenance
                    value:
                      - - name: id
                          value: integer
                        - name: revision
                          value: integer
                        - name: parents
                          value:
                            - - name: revision
                                value: integer
                              - name: id
                                value: integer
                              - name: index
                                value: integer
                        - name: type
                          value: string
            - name: error
              value:
                - name: details
                  value:
                    - object
                - name: message
                  value: string
                - name: code
                  value: integer
        - name: displayName
          value: string
        - name: name
          value: string
        - name: textExtractionDisabled
          value: boolean
        - name: properties
          value:
            - - name: textValues
                value:
                  - name: values
                    value:
                      - string
              - name: enumValues
                value:
                  - name: values
                    value:
                      - string
              - name: propertyValues
                value:
                  - name: properties
                    value:
                      - - name: timestampValues
                          value:
                            - name: values
                              value:
                                - - name: textValue
                                    value: string
                                  - name: timestampValue
                                    value: string
                        - name: floatValues
                          value:
                            - name: values
                              value:
                                - number
                        - name: mapProperty
                          value:
                            - name: fields
                              value: object
                        - name: integerValues
                          value:
                            - name: values
                              value:
                                - integer
                        - name: dateTimeValues
                          value:
                            - name: values
                              value:
                                - - name: day
                                    value: integer
                                  - name: hours
                                    value: integer
                                  - name: month
                                    value: integer
                                  - name: year
                                    value: integer
                                  - name: utcOffset
                                    value: string
                                  - name: minutes
                                    value: integer
                                  - name: nanos
                                    value: integer
                                  - name: seconds
                                    value: integer
                        - name: name
                          value: string
              - name: name
                value: string
        - name: textExtractionEnabled
          value: boolean
        - name: plainText
          value: string
        - name: updateTime
          value: string
        - name: rawDocumentPath
          value: string
        - name: displayUri
          value: string
        - name: dispositionTime
          value: string
        - name: documentSchemaName
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>documents</code> resource.

```sql
/*+ update */
UPDATE google.contentwarehouse.documents
SET 
cloudAiDocumentOption = '{{ cloudAiDocumentOption }}',
requestMetadata = '{{ requestMetadata }}',
document = '{{ document }}',
updateOptions = '{{ updateOptions }}'
WHERE 
documentsId = '{{ documentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>documents</code> resource.

```sql
/*+ delete */
DELETE FROM google.contentwarehouse.documents
WHERE documentsId = '{{ documentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
