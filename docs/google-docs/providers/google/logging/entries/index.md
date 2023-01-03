---
title: entries
hide_title: false
hide_table_of_contents: false
keywords:
  - entries
  - logging
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.entries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `operation` | `object` | Additional information about a potentially long-running operation with which a log entry is associated. |
| `traceSampled` | `boolean` | Optional. The sampling decision of the trace associated with the log entry.True means that the trace resource name in the trace field was sampled for storage in a trace backend. False means that the trace was not sampled for storage when this log entry was written, or the sampling decision was unknown at the time. A non-sampled trace value is still useful as a request correlation identifier. The default is False. |
| `trace` | `string` | Optional. Resource name of the trace associated with the log entry, if any. If it contains a relative resource name, the name is assumed to be relative to //tracing.googleapis.com. Example: projects/my-projectid/traces/06796866738c859f2f19b7cfb3214824 |
| `spanId` | `string` | Optional. The span ID within the trace associated with the log entry.For Trace spans, this is the same format that the Trace API v2 uses: a 16-character hexadecimal encoding of an 8-byte array, such as 000000000000004a. |
| `receiveTimestamp` | `string` | Output only. The time the log entry was received by Logging. |
| `httpRequest` | `object` | A common proto for logging HTTP requests. Only contains semantics defined by the HTTP specification. Product-specific logging information MUST be defined in a separate message. |
| `labels` | `object` | Optional. A map of key, value pairs that provides additional information about the log entry. The labels can be user-defined or system-defined.User-defined labels are arbitrary key, value pairs that you can use to classify logs.System-defined labels are defined by GCP services for platform logs. They have two components - a service namespace component and the attribute name. For example: compute.googleapis.com/resource_name.Cloud Logging truncates label keys that exceed 512 B and label values that exceed 64 KB upon their associated log entry being written. The truncation is indicated by an ellipsis at the end of the character string. |
| `protoPayload` | `object` | The log entry payload, represented as a protocol buffer. Some Google Cloud Platform services use this field for their log entry payloads.The following protocol buffer types are supported; user-defined types are not supported:"type.googleapis.com/google.cloud.audit.AuditLog" "type.googleapis.com/google.appengine.logging.v1.RequestLog" |
| `resource` | `object` | An object representing a resource that can be used for monitoring, logging, billing, or other purposes. Examples include virtual machine instances, databases, and storage devices such as disks. The type field identifies a MonitoredResourceDescriptor object that describes the resource's schema. Information in the labels field identifies the actual resource and its attributes according to the schema. For example, a particular Compute Engine VM instance could be represented by the following object, because the MonitoredResourceDescriptor for "gce_instance" has labels "project_id", "instance_id" and "zone": { "type": "gce_instance", "labels": { "project_id": "my-project", "instance_id": "12345678901234", "zone": "us-central1-a" }}  |
| `sourceLocation` | `object` | Additional information about the source code location that produced the log entry. |
| `jsonPayload` | `object` | The log entry payload, represented as a structure that is expressed as a JSON object. |
| `textPayload` | `string` | The log entry payload, represented as a Unicode string (UTF-8). |
| `timestamp` | `string` | Optional. The time the event described by the log entry occurred. This time is used to compute the log entry's age and to enforce the logs retention period. If this field is omitted in a new log entry, then Logging assigns it the current time. Timestamps have nanosecond accuracy, but trailing zeros in the fractional seconds might be omitted when the timestamp is displayed.Incoming log entries must have timestamps that don't exceed the logs retention period (https://cloud.google.com/logging/quotas#logs_retention_periods) in the past, and that don't exceed 24 hours in the future. Log entries outside those time boundaries aren't ingested by Logging. |
| `severity` | `string` | Optional. The severity of the log entry. The default value is LogSeverity.DEFAULT. |
| `split` | `object` | Additional information used to correlate multiple log entries. Used when a single LogEntry would exceed the Google Cloud Logging size limit and is split across multiple log entries. |
| `insertId` | `string` | Optional. A unique identifier for the log entry. If you provide a value, then Logging considers other log entries in the same project, with the same timestamp, and with the same insert_id to be duplicates which are removed in a single query result. However, there are no guarantees of de-duplication in the export of logs.If the insert_id is omitted when writing a log entry, the Logging API assigns its own unique identifier in this field.In queries, the insert_id is also used to order log entries that have the same log_name and timestamp values. |
| `metadata` | `object` | Auxiliary metadata for a MonitoredResource object. MonitoredResource objects contain the minimum set of information to uniquely identify a monitored resource instance. There is some other useful auxiliary metadata. Monitoring and Logging use an ingestion pipeline to extract metadata for cloud resources of all types, and store the metadata in this message. |
| `logName` | `string` | Required. The resource name of the log to which this log entry belongs: "projects/[PROJECT_ID]/logs/[LOG_ID]" "organizations/[ORGANIZATION_ID]/logs/[LOG_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]" "folders/[FOLDER_ID]/logs/[LOG_ID]" A project number may be used in place of PROJECT_ID. The project number is translated to its corresponding PROJECT_ID internally and the log_name field will contain PROJECT_ID in queries and exports.[LOG_ID] must be URL-encoded within log_name. Example: "organizations/1234567890/logs/cloudresourcemanager.googleapis.com%2Factivity".[LOG_ID] must be less than 512 characters long and can only include the following characters: upper and lower case alphanumeric characters, forward-slash, underscore, hyphen, and period.For backward compatibility, if log_name begins with a forward-slash, such as /projects/..., then the log entry is ingested as usual, but the forward-slash is removed. Listing the log entry will not show the leading slash and filtering for a log name with a leading slash will never return any results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` |  | Lists log entries. Use this method to retrieve log entries that originated from a project/folder/organization/billing account. For ways to export log entries, see Exporting Logs (https://cloud.google.com/logging/docs/export). |
| `copy` | `EXEC` |  | Copies a set of log entries from a log bucket to a Cloud Storage bucket. |
| `tail` | `EXEC` |  | Streaming read of log entries as they are ingested. Until the stream is terminated, it will continue reading logs. |
| `write` | `EXEC` |  | Writes log entries to Logging. This API method is the only way to send log entries to Logging. This method is used, directly or indirectly, by the Logging agent (fluentd) and all logging libraries configured to use Logging. A single request may contain log entries for a maximum of 1000 different resources (projects, organizations, billing accounts or folders) |
