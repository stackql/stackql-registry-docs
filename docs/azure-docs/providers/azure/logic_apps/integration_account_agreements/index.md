---
title: integration_account_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_agreements
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>integration_account_agreements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_account_agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_account_agreements" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_agreements', value: 'view', },
        { label: 'integration_account_agreements', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="agreementName" /> | `text` | field from the `properties` object |
| <CopyableCode code="agreement_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="changed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="content" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_partner" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_partner" /> | `text` | field from the `properties` object |
| <CopyableCode code="integrationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The integration account agreement properties. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agreementName, integrationAccountName, resourceGroupName, subscriptionId" /> | Gets an integration account agreement. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId" /> | Gets a list of integration account agreements. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="agreementName, integrationAccountName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an integration account agreement. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agreementName, integrationAccountName, resourceGroupName, subscriptionId" /> | Deletes an integration account agreement. |

## `SELECT` examples

Gets a list of integration account agreements.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_agreements', value: 'view', },
        { label: 'integration_account_agreements', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
agreementName,
agreement_type,
changed_time,
content,
created_time,
guest_identity,
guest_partner,
host_identity,
host_partner,
integrationAccountName,
location,
metadata,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.logic_apps.vw_integration_account_agreements
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.logic_apps.integration_account_agreements
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration_account_agreements</code> resource.

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
INSERT INTO azure.logic_apps.integration_account_agreements (
agreementName,
integrationAccountName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
location,
tags
)
SELECT 
'{{ agreementName }}',
'{{ integrationAccountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: createdTime
          value: string
        - name: changedTime
          value: string
        - name: metadata
          value: []
        - name: agreementType
          value: []
        - name: hostPartner
          value: string
        - name: guestPartner
          value: string
        - name: hostIdentity
          value:
            - name: qualifier
              value: string
            - name: value
              value: string
        - name: content
          value:
            - name: aS2
              value:
                - name: receiveAgreement
                  value:
                    - name: protocolSettings
                      value:
                        - name: messageConnectionSettings
                          value:
                            - name: ignoreCertificateNameMismatch
                              value: boolean
                            - name: supportHttpStatusCodeContinue
                              value: boolean
                            - name: keepHttpConnectionAlive
                              value: boolean
                            - name: unfoldHttpHeaders
                              value: boolean
                        - name: acknowledgementConnectionSettings
                          value:
                            - name: ignoreCertificateNameMismatch
                              value: boolean
                            - name: supportHttpStatusCodeContinue
                              value: boolean
                            - name: keepHttpConnectionAlive
                              value: boolean
                            - name: unfoldHttpHeaders
                              value: boolean
                        - name: mdnSettings
                          value:
                            - name: needMDN
                              value: boolean
                            - name: signMDN
                              value: boolean
                            - name: sendMDNAsynchronously
                              value: boolean
                            - name: receiptDeliveryUrl
                              value: string
                            - name: dispositionNotificationTo
                              value: string
                            - name: signOutboundMDNIfOptional
                              value: boolean
                            - name: mdnText
                              value: string
                            - name: sendInboundMDNToMessageBox
                              value: boolean
                            - name: micHashingAlgorithm
                              value: []
                        - name: securitySettings
                          value:
                            - name: overrideGroupSigningCertificate
                              value: boolean
                            - name: signingCertificateName
                              value: string
                            - name: encryptionCertificateName
                              value: string
                            - name: enableNRRForInboundEncodedMessages
                              value: boolean
                            - name: enableNRRForInboundDecodedMessages
                              value: boolean
                            - name: enableNRRForOutboundMDN
                              value: boolean
                            - name: enableNRRForOutboundEncodedMessages
                              value: boolean
                            - name: enableNRRForOutboundDecodedMessages
                              value: boolean
                            - name: enableNRRForInboundMDN
                              value: boolean
                            - name: sha2AlgorithmFormat
                              value: string
                        - name: validationSettings
                          value:
                            - name: overrideMessageProperties
                              value: boolean
                            - name: encryptMessage
                              value: boolean
                            - name: signMessage
                              value: boolean
                            - name: compressMessage
                              value: boolean
                            - name: checkDuplicateMessage
                              value: boolean
                            - name: interchangeDuplicatesValidityDays
                              value: integer
                            - name: checkCertificateRevocationListOnSend
                              value: boolean
                            - name: checkCertificateRevocationListOnReceive
                              value: boolean
                            - name: encryptionAlgorithm
                              value: []
                            - name: signingAlgorithm
                              value: []
                        - name: envelopeSettings
                          value:
                            - name: messageContentType
                              value: string
                            - name: transmitFileNameInMimeHeader
                              value: boolean
                            - name: fileNameTemplate
                              value: string
                            - name: suspendMessageOnFileNameGenerationError
                              value: boolean
                            - name: autogenerateFileName
                              value: boolean
                        - name: errorSettings
                          value:
                            - name: suspendDuplicateMessage
                              value: boolean
                            - name: resendIfMDNNotReceived
                              value: boolean
            - name: x12
              value:
                - name: receiveAgreement
                  value:
                    - name: protocolSettings
                      value:
                        - name: validationSettings
                          value:
                            - name: validateCharacterSet
                              value: boolean
                            - name: checkDuplicateInterchangeControlNumber
                              value: boolean
                            - name: interchangeControlNumberValidityDays
                              value: integer
                            - name: checkDuplicateGroupControlNumber
                              value: boolean
                            - name: checkDuplicateTransactionSetControlNumber
                              value: boolean
                            - name: validateEDITypes
                              value: boolean
                            - name: validateXSDTypes
                              value: boolean
                            - name: allowLeadingAndTrailingSpacesAndZeroes
                              value: boolean
                            - name: trimLeadingAndTrailingSpacesAndZeroes
                              value: boolean
                            - name: trailingSeparatorPolicy
                              value: []
                        - name: framingSettings
                          value:
                            - name: dataElementSeparator
                              value: integer
                            - name: componentSeparator
                              value: integer
                            - name: replaceSeparatorsInPayload
                              value: boolean
                            - name: replaceCharacter
                              value: integer
                            - name: segmentTerminator
                              value: integer
                            - name: characterSet
                              value: []
                            - name: segmentTerminatorSuffix
                              value: []
                        - name: envelopeSettings
                          value:
                            - name: controlStandardsId
                              value: integer
                            - name: useControlStandardsIdAsRepetitionCharacter
                              value: boolean
                            - name: senderApplicationId
                              value: string
                            - name: receiverApplicationId
                              value: string
                            - name: controlVersionNumber
                              value: string
                            - name: interchangeControlNumberLowerBound
                              value: integer
                            - name: interchangeControlNumberUpperBound
                              value: integer
                            - name: rolloverInterchangeControlNumber
                              value: boolean
                            - name: enableDefaultGroupHeaders
                              value: boolean
                            - name: functionalGroupId
                              value: string
                            - name: groupControlNumberLowerBound
                              value: integer
                            - name: groupControlNumberUpperBound
                              value: integer
                            - name: rolloverGroupControlNumber
                              value: boolean
                            - name: groupHeaderAgencyCode
                              value: string
                            - name: groupHeaderVersion
                              value: string
                            - name: transactionSetControlNumberLowerBound
                              value: integer
                            - name: transactionSetControlNumberUpperBound
                              value: integer
                            - name: rolloverTransactionSetControlNumber
                              value: boolean
                            - name: transactionSetControlNumberPrefix
                              value: string
                            - name: transactionSetControlNumberSuffix
                              value: string
                            - name: overwriteExistingTransactionSetControlNumber
                              value: boolean
                            - name: groupHeaderDateFormat
                              value: []
                            - name: groupHeaderTimeFormat
                              value: []
                            - name: usageIndicator
                              value: []
                        - name: acknowledgementSettings
                          value:
                            - name: needTechnicalAcknowledgement
                              value: boolean
                            - name: batchTechnicalAcknowledgements
                              value: boolean
                            - name: needFunctionalAcknowledgement
                              value: boolean
                            - name: functionalAcknowledgementVersion
                              value: string
                            - name: batchFunctionalAcknowledgements
                              value: boolean
                            - name: needImplementationAcknowledgement
                              value: boolean
                            - name: implementationAcknowledgementVersion
                              value: string
                            - name: batchImplementationAcknowledgements
                              value: boolean
                            - name: needLoopForValidMessages
                              value: boolean
                            - name: sendSynchronousAcknowledgement
                              value: boolean
                            - name: acknowledgementControlNumberPrefix
                              value: string
                            - name: acknowledgementControlNumberSuffix
                              value: string
                            - name: acknowledgementControlNumberLowerBound
                              value: integer
                            - name: acknowledgementControlNumberUpperBound
                              value: integer
                            - name: rolloverAcknowledgementControlNumber
                              value: boolean
                        - name: messageFilter
                          value:
                            - name: messageFilterType
                              value: []
                        - name: securitySettings
                          value:
                            - name: authorizationQualifier
                              value: string
                            - name: authorizationValue
                              value: string
                            - name: securityQualifier
                              value: string
                            - name: passwordValue
                              value: string
                        - name: processingSettings
                          value:
                            - name: maskSecurityInfo
                              value: boolean
                            - name: convertImpliedDecimal
                              value: boolean
                            - name: preserveInterchange
                              value: boolean
                            - name: suspendInterchangeOnError
                              value: boolean
                            - name: createEmptyXmlTagsForTrailingSeparators
                              value: boolean
                            - name: useDotAsDecimalSeparator
                              value: boolean
                        - name: envelopeOverrides
                          value:
                            - - name: targetNamespace
                                value: string
                              - name: protocolVersion
                                value: string
                              - name: messageId
                                value: string
                              - name: responsibleAgencyCode
                                value: string
                              - name: headerVersion
                                value: string
                              - name: senderApplicationId
                                value: string
                              - name: receiverApplicationId
                                value: string
                              - name: functionalIdentifierCode
                                value: string
                        - name: validationOverrides
                          value:
                            - - name: messageId
                                value: string
                              - name: validateEDITypes
                                value: boolean
                              - name: validateXSDTypes
                                value: boolean
                              - name: allowLeadingAndTrailingSpacesAndZeroes
                                value: boolean
                              - name: validateCharacterSet
                                value: boolean
                              - name: trimLeadingAndTrailingSpacesAndZeroes
                                value: boolean
                        - name: messageFilterList
                          value:
                            - - name: messageId
                                value: string
                        - name: schemaReferences
                          value:
                            - - name: messageId
                                value: string
                              - name: senderApplicationId
                                value: string
                              - name: schemaVersion
                                value: string
                              - name: schemaName
                                value: string
                        - name: x12DelimiterOverrides
                          value:
                            - - name: protocolVersion
                                value: string
                              - name: messageId
                                value: string
                              - name: dataElementSeparator
                                value: integer
                              - name: componentSeparator
                                value: integer
                              - name: segmentTerminator
                                value: integer
                              - name: replaceCharacter
                                value: integer
                              - name: replaceSeparatorsInPayload
                                value: boolean
                              - name: targetNamespace
                                value: string
            - name: edifact
              value:
                - name: receiveAgreement
                  value:
                    - name: protocolSettings
                      value:
                        - name: validationSettings
                          value:
                            - name: validateCharacterSet
                              value: boolean
                            - name: checkDuplicateInterchangeControlNumber
                              value: boolean
                            - name: interchangeControlNumberValidityDays
                              value: integer
                            - name: checkDuplicateGroupControlNumber
                              value: boolean
                            - name: checkDuplicateTransactionSetControlNumber
                              value: boolean
                            - name: validateEDITypes
                              value: boolean
                            - name: validateXSDTypes
                              value: boolean
                            - name: allowLeadingAndTrailingSpacesAndZeroes
                              value: boolean
                            - name: trimLeadingAndTrailingSpacesAndZeroes
                              value: boolean
                        - name: framingSettings
                          value:
                            - name: serviceCodeListDirectoryVersion
                              value: string
                            - name: characterEncoding
                              value: string
                            - name: protocolVersion
                              value: integer
                            - name: dataElementSeparator
                              value: integer
                            - name: componentSeparator
                              value: integer
                            - name: segmentTerminator
                              value: integer
                            - name: releaseIndicator
                              value: integer
                            - name: repetitionSeparator
                              value: integer
                            - name: characterSet
                              value: []
                            - name: decimalPointIndicator
                              value: []
                        - name: envelopeSettings
                          value:
                            - name: groupAssociationAssignedCode
                              value: string
                            - name: communicationAgreementId
                              value: string
                            - name: applyDelimiterStringAdvice
                              value: boolean
                            - name: createGroupingSegments
                              value: boolean
                            - name: enableDefaultGroupHeaders
                              value: boolean
                            - name: recipientReferencePasswordValue
                              value: string
                            - name: recipientReferencePasswordQualifier
                              value: string
                            - name: applicationReferenceId
                              value: string
                            - name: processingPriorityCode
                              value: string
                            - name: interchangeControlNumberLowerBound
                              value: integer
                            - name: interchangeControlNumberUpperBound
                              value: integer
                            - name: rolloverInterchangeControlNumber
                              value: boolean
                            - name: interchangeControlNumberPrefix
                              value: string
                            - name: interchangeControlNumberSuffix
                              value: string
                            - name: senderReverseRoutingAddress
                              value: string
                            - name: receiverReverseRoutingAddress
                              value: string
                            - name: functionalGroupId
                              value: string
                            - name: groupControllingAgencyCode
                              value: string
                            - name: groupMessageVersion
                              value: string
                            - name: groupMessageRelease
                              value: string
                            - name: groupControlNumberLowerBound
                              value: integer
                            - name: groupControlNumberUpperBound
                              value: integer
                            - name: rolloverGroupControlNumber
                              value: boolean
                            - name: groupControlNumberPrefix
                              value: string
                            - name: groupControlNumberSuffix
                              value: string
                            - name: groupApplicationReceiverQualifier
                              value: string
                            - name: groupApplicationReceiverId
                              value: string
                            - name: groupApplicationSenderQualifier
                              value: string
                            - name: groupApplicationSenderId
                              value: string
                            - name: groupApplicationPassword
                              value: string
                            - name: overwriteExistingTransactionSetControlNumber
                              value: boolean
                            - name: transactionSetControlNumberPrefix
                              value: string
                            - name: transactionSetControlNumberSuffix
                              value: string
                            - name: transactionSetControlNumberLowerBound
                              value: integer
                            - name: transactionSetControlNumberUpperBound
                              value: integer
                            - name: rolloverTransactionSetControlNumber
                              value: boolean
                            - name: isTestInterchange
                              value: boolean
                            - name: senderInternalIdentification
                              value: string
                            - name: senderInternalSubIdentification
                              value: string
                            - name: receiverInternalIdentification
                              value: string
                            - name: receiverInternalSubIdentification
                              value: string
                        - name: acknowledgementSettings
                          value:
                            - name: needTechnicalAcknowledgement
                              value: boolean
                            - name: batchTechnicalAcknowledgements
                              value: boolean
                            - name: needFunctionalAcknowledgement
                              value: boolean
                            - name: batchFunctionalAcknowledgements
                              value: boolean
                            - name: needLoopForValidMessages
                              value: boolean
                            - name: sendSynchronousAcknowledgement
                              value: boolean
                            - name: acknowledgementControlNumberPrefix
                              value: string
                            - name: acknowledgementControlNumberSuffix
                              value: string
                            - name: acknowledgementControlNumberLowerBound
                              value: integer
                            - name: acknowledgementControlNumberUpperBound
                              value: integer
                            - name: rolloverAcknowledgementControlNumber
                              value: boolean
                        - name: messageFilter
                          value: []
                        - name: processingSettings
                          value:
                            - name: maskSecurityInfo
                              value: boolean
                            - name: preserveInterchange
                              value: boolean
                            - name: suspendInterchangeOnError
                              value: boolean
                            - name: createEmptyXmlTagsForTrailingSeparators
                              value: boolean
                            - name: useDotAsDecimalSeparator
                              value: boolean
                        - name: envelopeOverrides
                          value:
                            - - name: messageId
                                value: string
                              - name: messageVersion
                                value: string
                              - name: messageRelease
                                value: string
                              - name: messageAssociationAssignedCode
                                value: string
                              - name: targetNamespace
                                value: string
                              - name: functionalGroupId
                                value: string
                              - name: senderApplicationQualifier
                                value: string
                              - name: senderApplicationId
                                value: string
                              - name: receiverApplicationQualifier
                                value: string
                              - name: receiverApplicationId
                                value: string
                              - name: controllingAgencyCode
                                value: string
                              - name: groupHeaderMessageVersion
                                value: string
                              - name: groupHeaderMessageRelease
                                value: string
                              - name: associationAssignedCode
                                value: string
                              - name: applicationPassword
                                value: string
                        - name: messageFilterList
                          value:
                            - - name: messageId
                                value: string
                        - name: schemaReferences
                          value:
                            - - name: messageId
                                value: string
                              - name: messageVersion
                                value: string
                              - name: messageRelease
                                value: string
                              - name: senderApplicationId
                                value: string
                              - name: senderApplicationQualifier
                                value: string
                              - name: associationAssignedCode
                                value: string
                              - name: schemaName
                                value: string
                        - name: validationOverrides
                          value:
                            - - name: messageId
                                value: string
                              - name: enforceCharacterSet
                                value: boolean
                              - name: validateEDITypes
                                value: boolean
                              - name: validateXSDTypes
                                value: boolean
                              - name: allowLeadingAndTrailingSpacesAndZeroes
                                value: boolean
                              - name: trimLeadingAndTrailingSpacesAndZeroes
                                value: boolean
                        - name: edifactDelimiterOverrides
                          value:
                            - - name: messageId
                                value: string
                              - name: messageVersion
                                value: string
                              - name: messageRelease
                                value: string
                              - name: dataElementSeparator
                                value: integer
                              - name: componentSeparator
                                value: integer
                              - name: segmentTerminator
                                value: integer
                              - name: repetitionSeparator
                                value: integer
                              - name: releaseIndicator
                                value: integer
                              - name: messageAssociationAssignedCode
                                value: string
                              - name: targetNamespace
                                value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>integration_account_agreements</code> resource.

```sql
/*+ delete */
DELETE FROM azure.logic_apps.integration_account_agreements
WHERE agreementName = '{{ agreementName }}'
AND integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
