---
title: log_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - log_entries
  - log_entries
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.log_entries.log_entries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="AnnotateLogEntry__type" /> | `string` |  |
| <CopyableCode code="AnnotateLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="AnnotateLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="AnnotateLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="AnnotateLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="AnnotateLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="AnnotateLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="AnnotateLogEntry_id" /> | `string` |  |
| <CopyableCode code="AnnotateLogEntry_incident" /> | `object` |  |
| <CopyableCode code="AnnotateLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="AnnotateLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="AnnotateLogEntry_service" /> | `object` |  |
| <CopyableCode code="AnnotateLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="AnnotateLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="AnnotateLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="AssignLogEntry__type" /> | `string` |  |
| <CopyableCode code="AssignLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="AssignLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="AssignLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="AssignLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="AssignLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="AssignLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="AssignLogEntry_id" /> | `string` |  |
| <CopyableCode code="AssignLogEntry_incident" /> | `object` |  |
| <CopyableCode code="AssignLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="AssignLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="AssignLogEntry_service" /> | `object` |  |
| <CopyableCode code="AssignLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="AssignLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="AssignLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="DelegateLogEntry__type" /> | `string` |  |
| <CopyableCode code="DelegateLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="DelegateLogEntry_assignees" /> | `array` | An array of assigned Users for this log entry |
| <CopyableCode code="DelegateLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="DelegateLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="DelegateLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="DelegateLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="DelegateLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="DelegateLogEntry_id" /> | `string` |  |
| <CopyableCode code="DelegateLogEntry_incident" /> | `object` |  |
| <CopyableCode code="DelegateLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="DelegateLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="DelegateLogEntry_service" /> | `object` |  |
| <CopyableCode code="DelegateLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="DelegateLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="DelegateLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="EscalateLogEntry__type" /> | `string` |  |
| <CopyableCode code="EscalateLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="EscalateLogEntry_assignees" /> | `array` | An array of assigned Users for this log entry |
| <CopyableCode code="EscalateLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="EscalateLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="EscalateLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="EscalateLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="EscalateLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="EscalateLogEntry_id" /> | `string` |  |
| <CopyableCode code="EscalateLogEntry_incident" /> | `object` |  |
| <CopyableCode code="EscalateLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="EscalateLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="EscalateLogEntry_service" /> | `object` |  |
| <CopyableCode code="EscalateLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="EscalateLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="EscalateLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="ExhaustEscalationPathLogEntry__type" /> | `string` |  |
| <CopyableCode code="ExhaustEscalationPathLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="ExhaustEscalationPathLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="ExhaustEscalationPathLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="ExhaustEscalationPathLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="ExhaustEscalationPathLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="ExhaustEscalationPathLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="ExhaustEscalationPathLogEntry_id" /> | `string` |  |
| <CopyableCode code="ExhaustEscalationPathLogEntry_incident" /> | `object` |  |
| <CopyableCode code="ExhaustEscalationPathLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="ExhaustEscalationPathLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="ExhaustEscalationPathLogEntry_service" /> | `object` |  |
| <CopyableCode code="ExhaustEscalationPathLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="ExhaustEscalationPathLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="ExhaustEscalationPathLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="NotifyLogEntry__type" /> | `string` |  |
| <CopyableCode code="NotifyLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="NotifyLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="NotifyLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="NotifyLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="NotifyLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="NotifyLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="NotifyLogEntry_id" /> | `string` |  |
| <CopyableCode code="NotifyLogEntry_incident" /> | `object` |  |
| <CopyableCode code="NotifyLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="NotifyLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="NotifyLogEntry_service" /> | `object` |  |
| <CopyableCode code="NotifyLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="NotifyLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="NotifyLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="ReachAckLimitLogEntry__type" /> | `string` |  |
| <CopyableCode code="ReachAckLimitLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="ReachAckLimitLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="ReachAckLimitLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="ReachAckLimitLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="ReachAckLimitLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="ReachAckLimitLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="ReachAckLimitLogEntry_id" /> | `string` |  |
| <CopyableCode code="ReachAckLimitLogEntry_incident" /> | `object` |  |
| <CopyableCode code="ReachAckLimitLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="ReachAckLimitLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="ReachAckLimitLogEntry_service" /> | `object` |  |
| <CopyableCode code="ReachAckLimitLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="ReachAckLimitLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="ReachAckLimitLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="ReachTriggerLimitLogEntry__type" /> | `string` |  |
| <CopyableCode code="ReachTriggerLimitLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="ReachTriggerLimitLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="ReachTriggerLimitLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="ReachTriggerLimitLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="ReachTriggerLimitLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="ReachTriggerLimitLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="ReachTriggerLimitLogEntry_id" /> | `string` |  |
| <CopyableCode code="ReachTriggerLimitLogEntry_incident" /> | `object` |  |
| <CopyableCode code="ReachTriggerLimitLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="ReachTriggerLimitLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="ReachTriggerLimitLogEntry_service" /> | `object` |  |
| <CopyableCode code="ReachTriggerLimitLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="ReachTriggerLimitLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="ReachTriggerLimitLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="RepeatEscalationPathLogEntry__type" /> | `string` |  |
| <CopyableCode code="RepeatEscalationPathLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="RepeatEscalationPathLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="RepeatEscalationPathLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="RepeatEscalationPathLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="RepeatEscalationPathLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="RepeatEscalationPathLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="RepeatEscalationPathLogEntry_id" /> | `string` |  |
| <CopyableCode code="RepeatEscalationPathLogEntry_incident" /> | `object` |  |
| <CopyableCode code="RepeatEscalationPathLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="RepeatEscalationPathLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="RepeatEscalationPathLogEntry_service" /> | `object` |  |
| <CopyableCode code="RepeatEscalationPathLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="RepeatEscalationPathLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="RepeatEscalationPathLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="ResolveLogEntry__type" /> | `string` |  |
| <CopyableCode code="ResolveLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="ResolveLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="ResolveLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="ResolveLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="ResolveLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="ResolveLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="ResolveLogEntry_id" /> | `string` |  |
| <CopyableCode code="ResolveLogEntry_incident" /> | `object` |  |
| <CopyableCode code="ResolveLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="ResolveLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="ResolveLogEntry_service" /> | `object` |  |
| <CopyableCode code="ResolveLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="ResolveLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="ResolveLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="SnoozeLogEntry__type" /> | `string` |  |
| <CopyableCode code="SnoozeLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="SnoozeLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="SnoozeLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="SnoozeLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="SnoozeLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="SnoozeLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="SnoozeLogEntry_id" /> | `string` |  |
| <CopyableCode code="SnoozeLogEntry_incident" /> | `object` |  |
| <CopyableCode code="SnoozeLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="SnoozeLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="SnoozeLogEntry_service" /> | `object` |  |
| <CopyableCode code="SnoozeLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="SnoozeLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="SnoozeLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="TriggerLogEntry__type" /> | `string` |  |
| <CopyableCode code="TriggerLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="TriggerLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="TriggerLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="TriggerLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="TriggerLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="TriggerLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="TriggerLogEntry_id" /> | `string` |  |
| <CopyableCode code="TriggerLogEntry_incident" /> | `object` |  |
| <CopyableCode code="TriggerLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="TriggerLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="TriggerLogEntry_service" /> | `object` |  |
| <CopyableCode code="TriggerLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="TriggerLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="TriggerLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="UnacknowledgeLogEntry__type" /> | `string` |  |
| <CopyableCode code="UnacknowledgeLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="UnacknowledgeLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="UnacknowledgeLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="UnacknowledgeLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="UnacknowledgeLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="UnacknowledgeLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="UnacknowledgeLogEntry_id" /> | `string` |  |
| <CopyableCode code="UnacknowledgeLogEntry_incident" /> | `object` |  |
| <CopyableCode code="UnacknowledgeLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="UnacknowledgeLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="UnacknowledgeLogEntry_service" /> | `object` |  |
| <CopyableCode code="UnacknowledgeLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="UnacknowledgeLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="UnacknowledgeLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="UrgencyChangeLogEntry__type" /> | `string` |  |
| <CopyableCode code="UrgencyChangeLogEntry_agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="UrgencyChangeLogEntry_channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="UrgencyChangeLogEntry_contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="UrgencyChangeLogEntry_created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="UrgencyChangeLogEntry_event_details" /> | `object` |  |
| <CopyableCode code="UrgencyChangeLogEntry_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="UrgencyChangeLogEntry_id" /> | `string` |  |
| <CopyableCode code="UrgencyChangeLogEntry_incident" /> | `object` |  |
| <CopyableCode code="UrgencyChangeLogEntry_note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="UrgencyChangeLogEntry_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="UrgencyChangeLogEntry_service" /> | `object` |  |
| <CopyableCode code="UrgencyChangeLogEntry_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="UrgencyChangeLogEntry_teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="UrgencyChangeLogEntry_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="_created_at" /> | `string` | Time at which the log entry was created |
| <CopyableCode code="_type" /> | `string` |  |
| <CopyableCode code="acknowledgement_timeout" /> | `integer` | Duration for which the acknowledgement lasts, in seconds. Services can contain an `acknowledgement_timeout` property, which specifies the length of time acknowledgements should last for. Each time an incident is acknowledged, this timeout is copied into the acknowledgement log entry. This property is optional, as older log entries may not contain it. It may also be `null`, as acknowledgements can be performed on incidents whose services have no `acknowledgement_timeout` set. |
| <CopyableCode code="agent" /> | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| <CopyableCode code="assignees" /> | `array` | An array of assigned Users for this log entry |
| <CopyableCode code="changed_actions" /> | `array` |  |
| <CopyableCode code="channel" /> | `object` | Polymorphic object representation of the means by which the action was channeled. Has different formats depending on type, indicated by channel[type]. Will be one of `auto`, `email`, `api`, `nagios`, or `timeout` if `agent[type]` is `service`. Will be one of `email`, `sms`, `website`, `web_trigger`, or `note` if `agent[type]` is `user`. See [below](https://developer.pagerduty.com/documentation/rest/log_entries/show#channel_types) for detailed information about channel formats. |
| <CopyableCode code="contexts" /> | `array` | Contexts to be included with the trigger such as links to graphs or images. |
| <CopyableCode code="created_at" /> | `string` | Time at which the log entry was created. |
| <CopyableCode code="event_details" /> | `object` |  |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="incident" /> | `object` |  |
| <CopyableCode code="note" /> | `string` | Optional field containing a note, if one was included with the log entry. |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="service" /> | `object` |  |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="teams" /> | `array` | Will consist of references unless included |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="user" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_log_entry" /> | `SELECT` | <CopyableCode code="id" /> | Get details for a specific incident log entry. This method provides additional information you can use to get at raw event data.<br /><br />A log of all the events that happen to an Incident, and these are exposed as Log Entries.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#log-entries)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| <CopyableCode code="list_log_entries" /> | `SELECT` |  | List all of the incident log entries across the entire account.<br /><br />A log of all the events that happen to an Incident, and these are exposed as Log Entries.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#log-entries)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| <CopyableCode code="_get_log_entry" /> | `EXEC` | <CopyableCode code="id" /> | Get details for a specific incident log entry. This method provides additional information you can use to get at raw event data.<br /><br />A log of all the events that happen to an Incident, and these are exposed as Log Entries.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#log-entries)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| <CopyableCode code="_list_log_entries" /> | `EXEC` |  | List all of the incident log entries across the entire account.<br /><br />A log of all the events that happen to an Incident, and these are exposed as Log Entries.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#log-entries)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| <CopyableCode code="update_log_entry_channel" /> | `EXEC` | <CopyableCode code="From, id, data__channel" /> | Update an existing incident log entry channel.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#log-entries)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |
