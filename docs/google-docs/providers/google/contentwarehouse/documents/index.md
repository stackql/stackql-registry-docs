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
cloudAiDocumentOption:
  customizedEntitiesPropertiesConversions: object
  enableEntitiesConversions: boolean
requestMetadata:
  userInfo:
    groupIds:
      - type: string
    id: string
policy:
  etag: string
  bindings:
    - members:
        - type: string
      role: string
      condition:
        location: string
        expression: string
        title: string
        description: string
  auditConfigs:
    - service: string
      auditLogConfigs:
        - exemptedMembers:
            - type: string
          logType: string
  version: integer
createMask: string
document:
  referenceId: string
  title: string
  updater: string
  creator: string
  rawDocumentFileType: string
  inlineRawDocument: string
  legalHold: boolean
  createTime: string
  contentCategory: string
  cloudAiDocument:
    revisions:
      - parent:
          - format: string
            type: string
        humanReview:
          state: string
          stateMessage: string
        id: string
        createTime: string
        processor: string
        parentIds:
          - type: string
        agent: string
    pages:
      - imageQualityScores:
          detectedDefects:
            - type: string
              confidence: number
          qualityScore: number
        tables:
          - layout:
              boundingPoly:
                normalizedVertices:
                  - 'y': number
                    x: number
                vertices:
                  - 'y': integer
                    x: integer
              orientation: string
              textAnchor:
                textSegments:
                  - startIndex: string
                    endIndex: string
                content: string
              confidence: number
            detectedLanguages:
              - languageCode: string
                confidence: number
            headerRows:
              - cells:
                  - colSpan: integer
                    detectedLanguages:
                      - languageCode: string
                        confidence: number
                    rowSpan: integer
            bodyRows:
              - cells:
                  - colSpan: integer
                    detectedLanguages:
                      - languageCode: string
                        confidence: number
                    rowSpan: integer
            provenance:
              id: integer
              revision: integer
              parents:
                - revision: integer
                  id: integer
                  index: integer
              type: string
        image:
          content: string
          width: integer
          mimeType: string
          height: integer
        formFields:
          - correctedKeyText: string
            valueDetectedLanguages:
              - languageCode: string
                confidence: number
            valueType: string
            nameDetectedLanguages:
              - languageCode: string
                confidence: number
            correctedValueText: string
        pageNumber: integer
        detectedBarcodes:
          - barcode:
              rawValue: string
              format: string
              valueFormat: string
        tokens:
          - detectedLanguages:
              - languageCode: string
                confidence: number
            detectedBreak:
              type: string
            styleInfo:
              textColor:
                green: number
                red: number
                alpha: number
                blue: number
              strikeout: boolean
              fontSize: integer
              underlined: boolean
              handwritten: boolean
              letterSpacing: number
              bold: boolean
              fontType: string
              fontWeight: integer
              smallcaps: boolean
              subscript: boolean
              pixelFontSize: number
              italic: boolean
              superscript: boolean
        detectedLanguages:
          - languageCode: string
            confidence: number
        symbols:
          - detectedLanguages:
              - languageCode: string
                confidence: number
        lines:
          - detectedLanguages:
              - languageCode: string
                confidence: number
        transforms:
          - type: integer
            data: string
            rows: integer
            cols: integer
        visualElements:
          - detectedLanguages:
              - languageCode: string
                confidence: number
            type: string
        paragraphs:
          - detectedLanguages:
              - languageCode: string
                confidence: number
        dimension:
          unit: string
          height: number
          width: number
        blocks:
          - detectedLanguages:
              - languageCode: string
                confidence: number
    entityRelations:
      - objectId: string
        relation: string
        subjectId: string
    content: string
    shardInfo:
      shardIndex: string
      shardCount: string
      textOffset: string
    chunkedDocument:
      chunks:
        - sourceBlockIds:
            - type: string
          pageFooters:
            - pageSpan:
                pageEnd: integer
                pageStart: integer
              text: string
          content: string
          chunkId: string
          pageHeaders:
            - text: string
    entities:
      - type: string
        normalizedValue:
          datetimeValue:
            day: integer
            hours: integer
            month: integer
            timeZone:
              version: string
              id: string
            year: integer
            utcOffset: string
            minutes: integer
            nanos: integer
            seconds: integer
          text: string
          moneyValue:
            nanos: integer
            currencyCode: string
            units: string
          booleanValue: boolean
          dateValue:
            year: integer
            day: integer
            month: integer
          integerValue: integer
          floatValue: number
          addressValue:
            revision: integer
            regionCode: string
            administrativeArea: string
            organization: string
            locality: string
            sortingCode: string
            sublocality: string
            addressLines:
              - type: string
            recipients:
              - type: string
            languageCode: string
            postalCode: string
        properties:
          - type: string
            properties:
              - type: string
                properties:
                  - type: string
                    properties:
                      - type: string
                        properties:
                          - type: string
                            properties:
                              - type: string
                                properties:
                                  - type: string
                                    properties:
                                      - {}
                                    id: string
                                    confidence: number
                                    redacted: boolean
                                    mentionText: string
                                    mentionId: string
                                    pageAnchor: {}
                                id: string
                                confidence: number
                                redacted: boolean
                                mentionText: string
                                mentionId: string
                            id: string
                            confidence: number
                            redacted: boolean
                            mentionText: string
                            mentionId: string
                        id: string
                        confidence: number
                        redacted: boolean
                        mentionText: string
                        mentionId: string
                    id: string
                    confidence: number
                    redacted: boolean
                    mentionText: string
                    mentionId: string
                id: string
                confidence: number
                redacted: boolean
                mentionText: string
                mentionId: string
            id: string
            confidence: number
            redacted: boolean
            mentionText: string
            mentionId: string
        id: string
        confidence: number
        redacted: boolean
        mentionText: string
        mentionId: string
    text: string
    textStyles:
      - fontWeight: string
        textStyle: string
        fontSize:
          unit: string
          size: number
        textDecoration: string
        fontFamily: string
    mimeType: string
    documentLayout:
      blocks:
        - pageSpan:
            pageStart: integer
            pageEnd: integer
          tableBlock:
            bodyRows:
              - cells:
                  - colSpan: integer
                    rowSpan: integer
                    blocks:
                      - listBlock:
                          listEntries:
                            - blocks:
                                - {}
                          type: string
                        blockId: string
                        textBlock:
                          text: string
                          type: string
                          blocks:
                            - blockId: string
            headerRows:
              - cells:
                  - colSpan: integer
                    rowSpan: integer
                    blocks:
                      - blockId: string
            caption: string
          blockId: string
    uri: string
    textChanges:
      - changedText: string
        provenance:
          - id: integer
            revision: integer
            parents:
              - revision: integer
                id: integer
                index: integer
            type: string
    error:
      details:
        - additionalProperties: any
          type: string
      message: string
      code: integer
  displayName: string
  name: string
  textExtractionDisabled: boolean
  properties:
    - textValues:
        values:
          - type: string
      enumValues:
        values:
          - type: string
      propertyValues:
        properties:
          - timestampValues:
              values:
                - textValue: string
                  timestampValue: string
            floatValues:
              values:
                - format: string
                  type: string
            mapProperty:
              fields: object
            integerValues:
              values:
                - format: string
                  type: string
            dateTimeValues:
              values:
                - day: integer
                  hours: integer
                  month: integer
                  year: integer
                  utcOffset: string
                  minutes: integer
                  nanos: integer
                  seconds: integer
            name: string
      name: string
  textExtractionEnabled: boolean
  plainText: string
  updateTime: string
  rawDocumentPath: string
  displayUri: string
  dispositionTime: string
  documentSchemaName: string

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
