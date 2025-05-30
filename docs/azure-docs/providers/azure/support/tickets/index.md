---
title: tickets
hide_title: false
hide_table_of_contents: false
keywords:
  - tickets
  - support
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

Creates, updates, deletes, gets or lists a <code>tickets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tickets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.tickets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tickets', value: 'view', },
        { label: 'tickets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Id of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="advanced_diagnostic_consent" /> | `text` | field from the `properties` object |
| <CopyableCode code="contact_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrollment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_workspace_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_temporary_ticket" /> | `text` | field from the `properties` object |
| <CopyableCode code="modified_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="problem_classification_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="problem_classification_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="problem_scoping_questions" /> | `text` | field from the `properties` object |
| <CopyableCode code="problem_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="quota_ticket_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="require24_x7_response" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_consent" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_level_agreement" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supportTicketName" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_engineer" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_plan_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_plan_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_plan_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_ticket_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="technical_ticket_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource 'Microsoft.Support/supportTickets'. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a support ticket. |
| <CopyableCode code="type" /> | `string` | Type of the resource 'Microsoft.Support/supportTickets'. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId, supportTicketName" /> | Get ticket details for an Azure subscription. Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the support tickets for an Azure subscription. You can also filter the support tickets by _Status_, _CreatedDate_, _ServiceId_, and _ProblemClassificationId_ using the $filter parameter. Output will be a paged result with _nextLink_, using which you can retrieve the next set of support tickets. <br/><br/>Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="subscriptionId, supportTicketName" /> | Creates a new support ticket for Subscription and Service limits (Quota), Technical, Billing, and Subscription Management issues for the specified subscription. Learn the [prerequisites](https://aka.ms/supportAPI) required to create a support ticket.<br/><br/>Always call the Services and ProblemClassifications API to get the most recent set of services and problem categories required for support ticket creation.<br/><br/>Adding attachments is not currently supported via the API. To add a file to an existing support ticket, visit the [Manage support ticket](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/managesupportrequest) page in the Azure portal, select the support ticket, and use the file upload control to add a new file.<br/><br/>Providing consent to share diagnostic information with Azure support is currently not supported via the API. The Azure support engineer working on your ticket will reach out to you for consent if your issue requires gathering diagnostic information from your Azure resources.<br/><br/>**Creating a support ticket for on-behalf-of**: Include _x-ms-authorization-auxiliary_ header to provide an auxiliary token as per [documentation](https://docs.microsoft.com/azure/azure-resource-manager/management/authenticate-multi-tenant). The primary token will be from the tenant for whom a support ticket is being raised against the subscription, i.e. Cloud solution provider (CSP) customer tenant. The auxiliary token will be from the Cloud solution provider (CSP) partner tenant. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="subscriptionId, supportTicketName" /> | This API allows you to update the severity level, ticket status, advanced diagnostic consent and your contact information in the support ticket.<br/><br/>Note: The severity levels cannot be changed if a support ticket is actively being worked upon by an Azure support engineer. In such a case, contact your support engineer to request severity update by adding a new communication using the Communications API. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Check the availability of a resource name. This API should be used to check the uniqueness of the name for support ticket creation for the selected subscription. |

## `SELECT` examples

Lists all the support tickets for an Azure subscription. You can also filter the support tickets by _Status_, _CreatedDate_, _ServiceId_, and _ProblemClassificationId_ using the $filter parameter. Output will be a paged result with _nextLink_, using which you can retrieve the next set of support tickets. <br/><br/>Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tickets', value: 'view', },
        { label: 'tickets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
advanced_diagnostic_consent,
contact_details,
created_date,
enrollment_id,
file_workspace_name,
is_temporary_ticket,
modified_date,
problem_classification_display_name,
problem_classification_id,
problem_scoping_questions,
problem_start_time,
quota_ticket_details,
require24_x7_response,
secondary_consent,
service_display_name,
service_id,
service_level_agreement,
severity,
status,
subscriptionId,
supportTicketName,
support_engineer,
support_plan_display_name,
support_plan_id,
support_plan_type,
support_ticket_id,
technical_ticket_details,
title,
type
FROM azure.support.vw_tickets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.support.tickets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tickets</code> resource.

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
INSERT INTO azure.support.tickets (
subscriptionId,
supportTicketName,
properties
)
SELECT 
'{{ subscriptionId }}',
'{{ supportTicketName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: supportTicketId
          value: string
        - name: description
          value: string
        - name: problemClassificationId
          value: string
        - name: problemClassificationDisplayName
          value: string
        - name: severity
          value: string
        - name: enrollmentId
          value: string
        - name: require24X7Response
          value: boolean
        - name: advancedDiagnosticConsent
          value: string
        - name: problemScopingQuestions
          value: string
        - name: supportPlanId
          value: string
        - name: contactDetails
          value:
            - name: firstName
              value: string
            - name: lastName
              value: string
            - name: preferredContactMethod
              value: string
            - name: primaryEmailAddress
              value: string
            - name: additionalEmailAddresses
              value:
                - string
            - name: phoneNumber
              value: string
            - name: preferredTimeZone
              value: string
            - name: country
              value: string
            - name: preferredSupportLanguage
              value: string
        - name: serviceLevelAgreement
          value:
            - name: startTime
              value: string
            - name: expirationTime
              value: string
            - name: slaMinutes
              value: integer
        - name: supportEngineer
          value:
            - name: emailAddress
              value: string
        - name: supportPlanType
          value: string
        - name: supportPlanDisplayName
          value: string
        - name: title
          value: string
        - name: problemStartTime
          value: string
        - name: serviceId
          value: string
        - name: serviceDisplayName
          value: string
        - name: status
          value: string
        - name: createdDate
          value: string
        - name: modifiedDate
          value: string
        - name: fileWorkspaceName
          value: string
        - name: isTemporaryTicket
          value: string
        - name: technicalTicketDetails
          value:
            - name: resourceId
              value: string
        - name: quotaTicketDetails
          value:
            - name: quotaChangeRequestSubType
              value: string
            - name: quotaChangeRequestVersion
              value: string
            - name: quotaChangeRequests
              value:
                - - name: region
                    value: string
                  - name: payload
                    value: string
        - name: secondaryConsent
          value:
            - - name: userConsent
                value: string
              - name: type
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tickets</code> resource.

```sql
/*+ update */
UPDATE azure.support.tickets
SET 
severity = '{{ severity }}',
status = '{{ status }}',
contactDetails = '{{ contactDetails }}',
advancedDiagnosticConsent = '{{ advancedDiagnosticConsent }}',
secondaryConsent = '{{ secondaryConsent }}'
WHERE 
subscriptionId = '{{ subscriptionId }}'
AND supportTicketName = '{{ supportTicketName }}';
```
